from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_glue as glue,
    aws_iam as iam,
)

class SimpleEtlPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket for raw data
        raw_data_bucket = s3.Bucket(self, 
            "RawDataBucket",
            removal_policy=core.RemovalPolicy.DESTROY,  # Only for dev/test
            auto_delete_objects=True  # Automatically delete objects in this bucket
        )

        # Create an S3 bucket for transformed data
        transformed_data_bucket = s3.Bucket(self, 
            "TransformedDataBucket",
            removal_policy=core.RemovalPolicy.DESTROY,  # Only for dev/test
            auto_delete_objects=True  # Automatically delete objects in this bucket
        )

        # IAM role for Glue job
        glue_role = iam.Role(self, "GlueJobRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole"),  # Attach Glue service role
            ],
        )

        # Glue job definition
        glue_job = glue.CfnJob(self, "SimpleETLJob",
            role=glue_role.role_arn,  # Assign the role to the Glue job
            command={
                "name": "glueetl",  # Type of job
                "script_location": f"s3://{raw_data_bucket.bucket_name}/scripts/etl_script.py",  # Path to your ETL script in S3
                "python_version": "3",  # Python version for the Glue job
            },
            default_arguments={
                "--TempDir": f"s3://{raw_data_bucket.bucket_name}/temp/",  # Temporary directory for Glue job
                "--job-bookmark-option": "job-bookmark-enable",  # Enable job bookmarks for incremental processing
            }
        )

        # Outputs
        core.CfnOutput(self, "RawDataBucketOutput", value=raw_data_bucket.bucket_name)  # Output the raw data bucket name
        core.CfnOutput(self, "TransformedDataBucketOutput", value=transformed_data_bucket.bucket_name)  # Output the transformed data bucket name
        core.CfnOutput(self, "GlueJobOutput", value=glue_job.ref)  # Output the Glue job reference
