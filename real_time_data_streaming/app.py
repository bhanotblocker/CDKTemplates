from aws_cdk import (
    core,
    aws_kinesis as kinesis,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
    aws_iam as iam,
)

class RealTimeDataStreamingStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Kinesis Stream
        stream = kinesis.Stream(
            self, "RealTimeStream",
            stream_name="RealTimeDataStream",
            shard_count=1
        )

        # Create Lambda Function
        lambda_function = _lambda.Function(
            self, "RealTimeDataProcessor",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",  # Point to the correct handler in lambda_function.py
            code=_lambda.Code.from_asset("real_time_data_streaming"),
            environment={
                "STREAM_NAME": stream.stream_name
            }
        )

        # Grant permissions to Lambda to read and write to the stream
        stream.grant_read(lambda_function)
        stream.grant_write(lambda_function)

        # Create an event source mapping to trigger the Lambda function from the Kinesis stream
        lambda_function.add_event_source(lambda_event_sources.KinesisEventSource(
            stream,
            starting_position=_lambda.StartingPosition.TRIM_HORIZON,
            batch_size=1  # Number of records to process at a time
        ))

app = core.App()
RealTimeDataStreamingStack(app, "RealTimeDataStreaming")
app.synth()
