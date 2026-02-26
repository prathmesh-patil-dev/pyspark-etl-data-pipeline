def load_data(df, output_path):
    df.write.mode("overwrite").csv(output_path, header=True)
