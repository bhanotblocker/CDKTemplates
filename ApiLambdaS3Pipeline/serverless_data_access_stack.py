from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
    aws_s3 as s3,
    core
)


class ServerlessDataAccessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # S3 Bucket for Data Storage
        data_bucket = s3.Bucket(
            self, 
            "DataBucket",
            versioned=True
        )

        # IAM Role for Lambda Function with S3 Access Permissions
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess")
            ]
        )

        # Lambda Function to Access Data in S3
        data_access_lambda = _lambda.Function(
            self, 
            "DataAccessFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.access.handler",
            code=_lambda.Code.from_asset("lambda"),
            role=lambda_role,
            environment={
                "BUCKET_NAME": data_bucket.bucket_name
            }
        )

        # Grant the Lambda Function Read Access to the S3 Bucket
        data_bucket.grant_read(lambda_role)

        # API Gateway to Trigger the Lambda Function
        api = apigw.LambdaRestApi(
            self, 
            "DataAccessAPI",
            handler=data_access_lambda,
            proxy=False
        )

        # Defining a Resource and Method for API Gateway
        data_resource = api.root.add_resource("data")
        data_resource.add_method("GET")  # GET /data
