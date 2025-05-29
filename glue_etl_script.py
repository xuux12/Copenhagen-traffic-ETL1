import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database = "traffic_db",
    table_name = "traffic_traffic_data",
    transformation_ctx = "datasource"
)

# Clean and transform data
cleaned_data = datasource.drop_nulls(['congestion_level'])

from pyspark.sql.functions import to_timestamp
df = cleaned_data.toDF()
df = df.withColumn("timestamp", to_timestamp("timestamp"))

cleaned_dynamic = DynamicFrame.fromDF(df, glueContext, "cleaned_dynamic")

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame = cleaned_dynamic,
    connection_type = "s3",
    connection_options = {"path": "s3://your-bucket-name/processed/"},
    format = "csv"
)

job.commit()
