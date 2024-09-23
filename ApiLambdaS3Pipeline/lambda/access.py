import boto3
import os
from botocore.exceptions import ClientError

s3_client = boto3.client("s3")
bucket_name = os.getenv("BUCKET_NAME")

def handler(event, context):
    try:
        # Example: List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return {
            "statusCode": 200,
            "body": response.get("Contents", [])
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
