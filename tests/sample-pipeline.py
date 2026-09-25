from pyspark import pipelines as dp
from pyspark.sql.functions import col


SOURCE_PATH = "/Volumes/factory_ops/raw/sensor_events"


@dp.table(name="sensor_readings_bronze")
def sensor_readings_bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load(SOURCE_PATH)
        .select(
            col("device_id"),
            col("event_time"),
            col("temperature_c"),
            col("vibration_mm_s"),
        )
    )
