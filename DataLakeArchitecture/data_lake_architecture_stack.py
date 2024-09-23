from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_glue as glue,
    aws_iam as iam,
    RemovalPolicy,
)
from constructs import Construct

class DataLakeArchitectureStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket for the data lake
        data_lake_bucket = s3.Bucket(
            self, "DataLakeBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Create an IAM role for AWS Glue
        glue_role = iam.Role(
            self, "GlueServiceRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")]
        )

        # Create a Glue database
        glue_database = glue.Database(
            self, "DataLakeDatabase",
            database_name="data_lake_db",
            location=data_lake_bucket.bucket_arn
        )

        # Outputs
        cdk.CfnOutput(self, "DataLakeBucketName", value=data_lake_bucket.bucket_name)
        cdk.CfnOutput(self, "GlueDatabaseName", value=glue_database.database_name)
