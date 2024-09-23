# Required IAM Permissions for Batch Processing Pipeline

To successfully deploy and run the Batch Processing Pipeline using AWS CDK, you need the following IAM permissions:

## S3 Permissions
- **s3:CreateBucket**: Allows the creation of an S3 bucket for input/output data.
- **s3:PutObject**: Allows writing objects to the S3 bucket.
- **s3:GetObject**: Allows reading objects from the S3 bucket.
- **s3:ListBucket**: Allows listing the contents of the S3 bucket.

## Batch Permissions
- **batch:CreateComputeEnvironment**: Allows creating a compute environment.
- **batch:CreateJobQueue**: Allows creating a job queue.
- **batch:RegisterJobDefinition**: Allows registering a job definition.
- **batch:SubmitJob**: Allows submitting jobs to the job queue.

## IAM Permissions
- **iam:CreateRole**: Allows creating a new IAM role for the Batch job.
- **iam:AttachRolePolicy**: Allows attaching the necessary managed policy to the IAM role.
- **iam:PassRole**: Allows passing the IAM role to AWS Batch.
