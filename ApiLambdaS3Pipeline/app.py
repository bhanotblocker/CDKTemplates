#!/usr/bin/env python3
import aws_cdk as cdk
from serverless_data_access_stack import ServerlessDataAccessStack

app = cdk.App()
ServerlessDataAccessStack(app, "ServerlessDataAccessStack")

app.synth()
