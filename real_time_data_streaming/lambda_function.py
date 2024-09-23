
#### 4. `lambda_function.py`

```python
import json
import boto3
import os

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the Kinesis data
        payload = json.loads(record['kinesis']['data'])
        print(f"Received data: {payload}")

        # Process the data (add your processing logic here)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully')
    }
