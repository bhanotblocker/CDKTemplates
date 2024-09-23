from aws_cdk import (
    aws_redshift as redshift,
    aws_s3 as s3,
    aws_iam as iam,
    aws_glue as glue,
    aws_ec2 as ec2,
    core
)

class RedshiftDataWarehouseStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket for ETL data storage
        etl_bucket = s3.Bucket(self, 
            "ETLDataBucket",
            versioned=True,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        # Create an IAM role for Redshift to access S3
        redshift_role = iam.Role(self, 
            "RedshiftRole",
            assumed_by=iam.ServicePrincipal("redshift.amazonaws.com")
        )
        
        # Grant S3 read/write permissions to Redshift
        etl_bucket.grant_read_write(redshift_role)
        
        # Attach AmazonS3ReadOnlyAccess policy (or more restrictive as needed)
        redshift_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess")
        )

        # VPC for the Redshift Cluster
        vpc = ec2.Vpc(self, "RedshiftVPC", max_azs=2)

        # Create a Redshift cluster
        redshift_cluster = redshift.Cluster(self, 
            "RedshiftCluster",
            master_user={
                "master_username": "admin",
                "master_password": core.SecretValue.plain_text("YourStrongPassword1")  # Change the password
            },
            vpc=vpc,
            cluster_type=redshift.ClusterType.MULTI_NODE,
            node_type=redshift.NodeType.DC2_LARGE,
            number_of_nodes=2,
            roles=[redshift_role]
        )

        # Optionally, create a Glue Crawler for ETL (Optional)
        glue_role = iam.Role(self, 
            "GlueServiceRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com")
        )

        glue_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")
        )
        
        # Allow Glue to read from the bucket
        etl_bucket.grant_read(glue_role)
        
        glue_database = glue.Database(self, 
            "ETLDatabase",
            database_name="etl_database"
        )

        glue_crawler = glue.CfnCrawler(self, 
            "ETLCrawler",
            role=glue_role.role_arn,
            database_name=glue_database.database_name,
            targets={
                "s3Targets": [{"path": etl_bucket.bucket_arn}]
            }
        )

        # Outputs
        core.CfnOutput(self, 
            "RedshiftClusterEndpoint",
            value=redshift_cluster.cluster_endpoint.hostname
        )
        core.CfnOutput(self, 
            "RedshiftIAMRoleArn",
            value=redshift_role.role_arn
        )
        core.CfnOutput(self, 
            "ETLS3Bucket",
            value=etl_bucket.bucket_name
        )
