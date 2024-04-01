import pandas as pd
import json
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def parse_text_file(text_file):
    products = []
    try:
        with open(text_file, 'r') as file:
            lines = file.readlines()
            logger.info(f"Reading products from text file '{text_file}'")
            i = 0
            while i < len(lines):
                product_id, name, price, in_stock = None, None, None, None
                product_info_cnt = 0
                if lines[i].strip().startswith("Product ID:"):
                    product_id = lines[i].split(': ')[1].strip()
                    i += 1
                    product_info_cnt += 1
                if lines[i].strip().startswith("Name:"):
                    name = lines[i].split(':')[1].strip()
                    i += 1
                    product_info_cnt += 1
                if lines[i].strip().startswith("Price:"):
                    price = lines[i].split(':')[1].strip()
                    i += 1
                    product_info_cnt += 1
                if lines[i].strip().startswith("In Stock:"):
                    in_stock = lines[i].split(':')[1].strip()
                    i += 1
                    product_info_cnt += 1

                if product_info_cnt == 4:
                    product = {
                        "ProductID": product_id,
                        "Name": name,
                        "Price": price,
                        "InStock": in_stock
                    }
                    products.append(product)
                else:
                    # going to the next product
                    while i < len(lines) and not lines[i].startswith("Product ID:"):
                        i += 1
    except FileNotFoundError as e:
        logger.error(f"Error: File '{text_file}' not found: {e.strerror}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    if len(products) > 0:
        logger.info(f"Successfully parsed {len(products)} products from the text file.")
    return products


def parse_csv_file(csv_file):
    products = []
    try:
        df = pd.read_csv(csv_file, dtype=str, on_bad_lines='skip', sep=',')
        df.fillna('', inplace=True)
        # Check if all required columns are present
        required_columns = ["ProductID", "Name", "Price", "InStock"]
        missing_columns = set(required_columns) - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns in CSV file: {missing_columns}")
        # Iterate over each row
        for index, row in df.iterrows():
            product_data = {}
            for column in required_columns:
                # Check if column exists in the row
                if column in df.columns:
                    value = row[column]
                    product_data[column] = str(value).strip()
                else:
                    logger.warning(f"Column '{column}' not found in row {index + 1}")
            # Append product data to products list
            products.append(product_data)
    except FileNotFoundError as e:
        logger.error(f"Error: File '{csv_file}' not found: {e}")
    except Exception as e:
        # Handle other unexpected errors
        logger.error(f"An error occurred: {e}")
    if len(products) > 0:
        logger.info(f"Successfully parsed {len(products)} products from the CSV file.")
    return products


def main(text_file, csv_file):
    text_products = parse_text_file(text_file)
    csv_products = parse_csv_file(csv_file)

    all_products = text_products + csv_products
    output_file = "output_products.json"

    if len(all_products) == 0:
        logger.info("No products found in final parsed file.")
        return
    else:
        logger.info(f"Total {len(all_products)} products has been parsed successfully from Text and CSV file.")
        logger.info("Total Products in final parsed file :")
        for product in all_products:
            logger.info(product)
        with open(output_file, 'w') as file:
            try:
                json.dump(all_products, file, indent=4)
                logger.info(f"Products saved to '{output_file}'")
            except Exception as e:
                logger.error(f"An error occurred while writing to JSON file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        logger.error("Usage: Invalid number of arguments. Please provide the text file and CSV file paths only.")
        logger.info("Sample Command: python script.py <text_file> <csv_file>")
        sys.exit(1)
    if not sys.argv[1].endswith(".txt"):
        logger.error("Error: The first file must be a text file.")
        sys.exit(1)
    if not sys.argv[2].endswith(".csv"):
        logger.error("Error: The second file must be a CSV file.")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
