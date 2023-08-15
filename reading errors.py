# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:13:49 2023

@author: hodan
"""
import csv
import openpyxl

def get_value_from_csv(file_path, row_index, column_index):
    try:
        # Read data from the CSV file
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row_num, row in enumerate(csvreader, start=1):
                if row_num == row_index:
                    return row[column_index - 1]
        return None
    except Exception as e:
        print("Error occurred:", e)
        return None

def write_value_to_excel(file_path, sheet_name, row_index, column_index, value):
    try:
        # Load the workbook
        workbook = openpyxl.load_workbook(file_path)

        # Select the sheet by name
        sheet = workbook[sheet_name]

        # Write the value to the specified cell
        sheet.cell(row=row_index, column=column_index, value=value)

        # Save the changes to the workbook
        workbook.save(file_path)

        # Close the workbook
        workbook.close()

        print("Value saved successfully.")
    except Exception as e:
        print("Error occurred:", e)

# Usage example
csv_file_path =  'C:/Users/hodan/OneDrive/Desktop/Video codesl/20191112-110011PST_Free Form_Trial2.csv'
row_index = 10  # Replace this with the row number (1-indexed)
column_index = 2  # Replace this with the column number (1-indexed)

# Get the value from the original Excel file
# Get the value from the CSV file
value_to_save = get_value_from_csv(csv_file_path, row_index, column_index)
#
#if value_to_save is not None:
#    print("Value at row {} and column {}: {}".format(row_index, column_index, value_to_save))
#
#    # Save the value to another Excel file at a specific location
#    output_file_path = 'path/to/your/output/excel/file.xlsx'  # Replace with the desired output file path
#    output_sheet_name = 'OutputSheet'  # Replace with the desired output sheet name
#    output_row_index = 5  # Replace this with the desired row number (1-indexed)
#    output_column_index = 4  # Replace this with the desired column number (1-indexed)
#    
#    write_value_to_excel(output_file_path, output_sheet_name, output_row_index, output_column_index, value_to_save)
#else:
#    print("Unable to retrieve the value.")
