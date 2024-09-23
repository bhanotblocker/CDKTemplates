import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the job name and other parameters from command line arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'DATABASE_NAME', 'TABLE_NAME', 'OUTPUT_BUCKET'])
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Example ETL logic
try:
    # Create a DynamicFrame from a Glue catalog table
    datasource = glueContext.create_dynamic_frame.from_catalog(database=args['DATABASE_NAME'], table_name=args['TABLE_NAME'])
    
    logger.info("Data extracted successfully from Glue catalog.")

    # Transform the data
    transformed_data = datasource.apply_mapping([
        ("old_column", "string", "new_column", "string")  # Adjust as necessary
    ])
    
    logger.info("Data transformation completed.")

    # Write the transformed data back to S3
    output_path = f"s3://{args['OUTPUT_BUCKET']}/output/"
    glueContext.write_dynamic_frame.to_s3(transformed_data, output_path)
    
    logger.info("Transformed data written to S3 successfully.")

except Exception as e:
    logger.error(f"Error during ETL job: {e}")
    sys.exit(1)
