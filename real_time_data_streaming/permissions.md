# Required IAM Permissions for Real-Time Data Streaming

To successfully deploy and run the Real-Time Data Streaming application using AWS CDK, you need the following IAM permissions:

## Kinesis Permissions
- **kinesis:CreateStream**: Allows the creation of Kinesis streams.
- **kinesis:PutRecord**: Allows sending data to the Kinesis stream.
- **kinesis:GetRecords**: Allows reading data from the Kinesis stream.

## Lambda Permissions
- **lambda:CreateFunction**: Allows the creation of a Lambda function.
- **lambda:UpdateFunctionCode**: Allows updating the code of an existing Lambda function.
- **lambda:AddPermission**: Allows adding permissions to the Lambda function.

## IAM Permissions
- **iam:CreateRole**: Allows creating a new IAM role for the Lambda function.
- **iam:AttachRolePolicy**: Allows attaching the necessary managed policy to the IAM role.
- **iam:PassRole**: Allows passing the IAM role to AWS Lambda.

## Example IAM Policy
Here is an example IAM policy that includes the necessary permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kinesis:CreateStream",
        "kinesis:PutRecord",
        "kinesis:GetRecords"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "lambda:CreateFunction",
        "lambda:UpdateFunctionCode",
        "lambda:AddPermission"
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
    }
  ]
}
