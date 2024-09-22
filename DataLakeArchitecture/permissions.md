# Required IAM Permissions for Data Lake Architecture

To successfully deploy and run the Data Lake Architecture using AWS CDK, you need the following IAM permissions:

## S3 Permissions
- **s3:CreateBucket**: Allows the creation of S3 buckets for storing raw and processed data.
- **s3:PutObject**: Allows writing objects to the S3 buckets.
- **s3:GetObject**: Allows reading objects from the S3 buckets.
- **s3:ListBucket**: Allows listing the contents of the S3 buckets.

## Glue Permissions
- **glue:CreateDatabase**: Allows creating a new Glue database.
- **glue:CreateTable**: Allows creating tables in the Glue data catalog.
- **glue:GetDatabase**: Allows fetching details about Glue catalog databases.
- **glue:GetTable**: Allows fetching details about Glue catalog tables.
- **glue:CreateCrawler**: Allows creating Glue crawlers to discover data in S3.
- **glue:StartCrawler**: Allows starting a Glue crawler.

## Athena Permissions
- **athena:StartQueryExecution**: Allows executing queries in Athena.
- **athena:GetQueryExecution**: Allows fetching details about query executions.
- **athena:GetQueryResults**: Allows retrieving the results of executed queries.

## IAM Permissions
- **iam:CreateRole**: Allows creating a new IAM role for Glue and Athena.
- **iam:AttachRolePolicy**: Allows attaching the necessary managed policy to the IAM role.
- **iam:PassRole**: Allows passing the IAM role to AWS Glue and Athena.

## Additional Permissions
- **logs:CreateLogGroup**: Allows creating CloudWatch log groups for logging Glue and Athena operations.
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
        "glue:CreateDatabase",
        "glue:CreateTable",
        "glue:GetDatabase",
        "glue:GetTable",
        "glue:CreateCrawler",
        "glue:StartCrawler"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "athena:StartQueryExecution",
        "athena:GetQueryExecution",
        "athena:GetQueryResults"
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
