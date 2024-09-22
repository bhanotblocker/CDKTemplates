# Simple ETL Pipeline with AWS CDK

## Overview

This repository contains a template for creating a Simple ETL (Extract, Transform, Load) Pipeline using AWS CDK in Python. The pipeline leverages AWS Glue for data transformation and Amazon S3 for data storage. This template serves as a foundational setup to help data engineers quickly establish ETL processes.

## Use Case Description

The Simple ETL Pipeline is designed to automate the process of extracting data from a source location, transforming it to meet specific requirements, and loading it into a target location for further analysis or processing. This is a common scenario in data engineering where clean and structured data is essential for analytics and reporting.

### Key Components

- **AWS Glue**: A fully managed ETL service that simplifies data preparation. In this use case, Glue jobs are used to perform the transformation of the data.
- **Amazon S3**: A scalable storage service used to store both the raw source data and the transformed output data.


### File Explanations

- **`cdk_app.py`**: This is the main entry point of your AWS CDK application. It defines the resources that will be provisioned in AWS, including Glue jobs and S3 buckets. Modify this file to set up your infrastructure.

- **`requirements.txt`**: A file that lists the Python packages required for your ETL script. Make sure to include `boto3` for AWS service interactions.

- **`permissions.md`**: A separate file detailing the IAM permissions required to execute the ETL pipeline successfully. This includes permissions for S3 and Glue.

- **`etl_scripts.py`**: This script contains the logic for the ETL process. You will place your extraction, transformation, and loading code here. Ensure that this file is referenced correctly in your CDK stack definition.

## Getting Started

### Prerequisites

- AWS account with access to AWS Glue and S3.
- AWS CLI configured with your credentials.
- Python environment set up with AWS CDK installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


![Simple ETL Pipeline Diagram](./images/etl_diagram.png)



