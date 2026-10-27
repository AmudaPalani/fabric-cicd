# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

from pyspark.sql import Row
from pyspark.sql import functions as F

version = "v1"

sales = spark.createDataFrame([
    Row(region="East", product="Laptop", amount=1200),
    Row(region="West", product="Laptop", amount=1500),
    Row(region="East", product="Monitor", amount=300),
    Row(region="West", product="Monitor", amount=450),
])

summary = (
    sales.groupBy("region")
    .agg(F.sum("amount").alias("total_sales"))
    .withColumn("pipeline_version", F.lit(version))
    .withColumn("processed_at", F.current_timestamp())
)

summary.write.mode("overwrite").format("delta").saveAsTable("sales_summary")

display(spark.table("sales_summary").orderBy("region"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }