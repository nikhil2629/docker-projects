import csv
import os

# Function to read data from a text file
def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Clean up the lines and return as a list of lists
        data = [line.strip().split(',') for line in lines]  # Assuming comma-separated data
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
        return []

# Function to write data to a CSV file
def write_to_csv(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data has been written to {file_path}")

# Paths for input TXT file and output CSV file
#input_txt_path = r"C:\Users\iamni\Documents\Untitled.txt"  # Specify the path to your input TXT file
#output_csv_path = r"C:\Users\iamni\Documents\output.csv"  # Specify the path for your output CSV file
#input_txt_path = "/app/input-output/Untitled.txt"  # Input file inside the container
#output_csv_path = "/app/input-output/output.csv"  # Output file inside the container
input_txt_path = "/home/nikbee/PyScript/Untitled.txt"  # Input file inside the container
output_csv_path = "/home/nikbee/PyScript/output.csv"  # Output file inside the container
# Transfer data
data = read_txt_file(input_txt_path)
if data:  # Proceed only if data is successfully read
    write_to_csv(output_csv_path, data)
