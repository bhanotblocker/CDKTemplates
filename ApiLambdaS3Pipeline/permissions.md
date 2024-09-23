# Required IAM Permissions

## IAM Role for Lambda
The IAM role attached to the Lambda function needs the following managed policies:

1. **AWSLambdaBasicExecutionRole**:
   - Allows the Lambda function to write logs to Amazon CloudWatch.

2. **AmazonS3ReadOnlyAccess**:
   - Grants the Lambda function read-only access to the S3 bucket.

## API Gateway Permissions
API Gateway requires permissions to invoke the Lambda function.

1. **Execute API**:
   - API Gateway needs permissions to execute the Lambda function.

### Additional Considerations
- Ensure the S3 bucket has the necessary permissions to allow the Lambda function to read objects.
- Configure IAM roles and policies in a way that follows the principle of least privilege.
