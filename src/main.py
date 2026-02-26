from pyspark.sql import SparkSession
from extract import extract_data
from transform import transform_data
from load import load_data
from config.config_dev import INPUT_PATH, OUTPUT_PATH

def main():
    spark = SparkSession.builder \
        .appName("Enterprise ETL Pipeline") \
        .getOrCreate()

    df = extract_data(spark, INPUT_PATH)
    transformed_df = transform_data(df)
    load_data(transformed_df, OUTPUT_PATH)

    spark.stop()

if __name__ == "__main__":
    main()
