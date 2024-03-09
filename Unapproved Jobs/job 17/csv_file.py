import pandas as pd


def main():
    file_path = "stock/StockEtablissement_utf8.csv"
    text_file_path = "stock/extract_siret.txt"
    required_siret = []
    result_df = pd.DataFrame()
    count = 0

    with open(text_file_path, 'r') as text_file:
    # Loop through each line in the text file
            for line in text_file:
                # print(line)
                required_siret.append(int(line.strip()))  #

    print("Siret Loaded")

    # Read the CSV file into a pandas DataFrame
    chunk_size = 10000  # Adjust this value according to your needs
    chunks = pd.read_csv(file_path, chunksize=chunk_size)

    # Process each chunk
    for chunk in chunks:
        found_rows = chunk[chunk['siret'].isin(required_siret)]
        result_df = result_df.append(found_rows, ignore_index=True)

        for index, row in found_rows.iterrows():
            count += 1
            print(count)

    result_df.to_csv("filtered_rows.csv", index=False)


if __name__ == "__main__":
    main()