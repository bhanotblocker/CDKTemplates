#!/usr/bin/env python3
import os
from aws_cdk import core
from simple_etl_pipeline.simple_etl_pipeline_stack import SimpleEtlPipelineStack

app = core.App()
SimpleEtlPipelineStack(app, "SimpleEtlPipelineStack")

app.synth()
