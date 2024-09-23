#!/usr/bin/env python3
import aws_cdk as cdk
from redshift_data_warehouse_stack import RedshiftDataWarehouseStack

app = cdk.App()
RedshiftDataWarehouseStack(app, "RedshiftDataWarehouseStack")

app.synth()
