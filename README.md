**FileParser**  
FileParser project is an implementation of a Python script that reads product information from a text file and a CSV file, merges the data, and outputs the result to the console and a JSON file.

To run the provided code, follow these steps:
1. Clone the repository to your local machine.  
	https://github.com/ankgupta16/FileParser.git
2. Navigate to the directory containing the Python script and input files.
3. go to the project directory  
   cd FileParser
4. install the required packages  
   pip install -r requirements.txt
5. Prepare Input Files: Ensure you have the required input files in the specified format. The script expects two input files in project directory  
	1.1. A text file containing product information in the specified format.  
		Product ID: 12345  
		Name: Product Name  
		Price: $19.99  
		In Stock: Yes  
	1.2. A CSV file containing product information with columns: ProductID, Name, Price, InStock.  
		The CSV file contains product information in the following columns: ProductID, Name, Price, InStock.  
6. Open the terminal or command prompt and navigate to the directory containing the Python script and input files.
7. Execute the Script: Run the script by executing the command:  
      **python product_parser.py <text_file_path> <csv_file_path>**
8. View the Output: The script will parse the input files, merge the product data, and output the result to the console as well as save it to a JSON file named output_products.json in the same directory as the script.  
9. Review the Output: Check the console output and the generated JSON file to view the merged product data.
10. For reference, the sample input files are provided in the repository for testing the script.  
   **Sample Command with Sample Input Files: python product_parser.py sample_text_file.txt sample_csv_file.csv**

11. **Development Environment**  
Python 3.9.7