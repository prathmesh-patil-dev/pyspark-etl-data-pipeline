def transform_data(df):
    df = df.dropDuplicates()
    df = df.dropna()
    return df
