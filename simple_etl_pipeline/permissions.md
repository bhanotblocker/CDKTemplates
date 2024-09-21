# Required IAM Permissions for Simple ETL Pipeline

To successfully deploy and run the Simple ETL Pipeline using AWS CDK, you need the following IAM permissions:

## S3 Permissions
- **s3:CreateBucket**: Allows the creation of S3 buckets for raw and transformed data.
- **s3:PutObject**: Allows writing objects to the S3 buckets.
- **s3:GetObject**: Allows reading objects from the S3 buckets.
- **s3:ListBucket**: Allows listing the contents of the S3 buckets.

## Glue Permissions
- **glue:CreateJob**: Allows creating a Glue job.
- **glue:UpdateJob**: Allows updating an existing Glue job.
- **glue:GetJob**: Allows fetching details about a Glue job.
- **glue:StartJobRun**: Allows starting a Glue job run.
- **glue:GetJobRun**: Allows fetching details about a job run.
- **glue:GetTable**: Allows fetching details about Glue catalog tables.
- **glue:GetDatabase**: Allows fetching details about Glue catalog databases.

## IAM Permissions
- **iam:CreateRole**: Allows creating a new IAM role for the Glue job.
- **iam:AttachRolePolicy**: Allows attaching the necessary managed policy to the IAM role.
- **iam:PassRole**: Allows passing the IAM role to AWS Glue.

## Additional Permissions
- **logs:CreateLogGroup**: Allows creating CloudWatch log groups for logging Glue job executions.
- **logs:CreateLogStream**: Allows creating CloudWatch log streams.
- **logs:PutLogEvents**: Allows writing log events to CloudWatch.

## Example IAM Policy
Here is an example IAM policy that includes the necessary permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:CreateBucket",
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "glue:CreateJob",
        "glue:UpdateJob",
        "glue:GetJob",
        "glue:StartJobRun",
        "glue:GetJobRun",
        "glue:GetTable",
        "glue:GetDatabase"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateRole",
        "iam:AttachRolePolicy",
        "iam:PassRole"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
