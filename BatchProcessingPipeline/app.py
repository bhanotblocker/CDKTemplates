from aws_cdk import App
from batch_processing_pipeline_stack import BatchProcessingPipelineStack

app = App()
BatchProcessingPipelineStack(app, "BatchProcessingPipeline")

app.synth()
