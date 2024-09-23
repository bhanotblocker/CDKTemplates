from aws_cdk import (
    Stack,
    aws_batch as batch,
    aws_s3 as s3,
    aws_iam as iam,
    aws_ec2 as ec2,
)
from constructs import Construct

class BatchProcessingPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket for input/output data
        bucket = s3.Bucket(self, "BatchInputOutputBucket")

        # Create a VPC
        vpc = ec2.Vpc(self, "BatchVpc")

        # Define the job role for AWS Batch
        job_role = iam.Role(self, "BatchJobRole",
                            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSBatchServiceRole")]
                            )
        
        # Create a compute environment
        compute_environment = batch.ComputeEnvironment(self, "BatchComputeEnvironment",
            managed=True,
            compute_resources=batch.ComputeResources(
                type=batch.ComputeResourceType.EC2,
                vpc=vpc,
                instance_types=[ec2.InstanceType("t2.micro")],
                minv_cpus=0,
                max_v_cpus=2,
            )
        )

        # Create a job queue
        job_queue = batch.JobQueue(self, "BatchJobQueue",
            priority=1,
            compute_environments=[batch.JobQueueComputeEnvironment(
                compute_environment=compute_environment,
                order=1
            )]
        )

        # Define a batch job definition
        job_definition = batch.JobDefinition(self, "BatchJobDefinition",
            container=batch.JobDefinitionContainer(
                image=batch.ContainerImage.from_registry("amazonlinux"),  # Use an appropriate image for your processing
                memory_limit_mib=512,
                vcpus=1,
                command=["echo", "Hello from Batch!"],
                job_role=job_role
            )
        )

        # Output the bucket name
        self.output_bucket_name = bucket.bucket_name
