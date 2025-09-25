from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count

# Initialize Spark
spark = SparkSession.builder.appName("OrderAnalysis").getOrCreate()

# Load cleaned dataset from Week 2
df = spark.read.csv("cleaned_orders.csv", header=True, inferSchema=True)

# Add delayed flag in Spark (redundant if already exists, but for demo)
df = df.withColumn("delayed", when(col("delay_days") > 0, 1).otherwise(0))

# Group by customer region (city/state) to count delays
delays_by_region = df.groupBy("city", "state").agg(count(when(col("delayed") == 1, True)).alias("delayed_orders"))

# Show results
delays_by_region.show(truncate=False)

# Save output
delays_by_region.coalesce(1).write.csv("delays_by_region_output", header=True, mode="overwrite")

spark.stop()
