from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    input_path = "data/raw/sample.csv"
    output_path = "data/processed/"

    df = extract_data(input_path)
    transformed_df = transform_data(df)
    load_data(transformed_df, output_path)

if __name__ == "__main__":
    main()
