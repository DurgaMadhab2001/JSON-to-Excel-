import pandas as pd

def json_to_excel(json_file, excel_file):
    df = pd.read_json(json_file)
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    input_json_file = "C:\Users\sarth\Desktop\AARSHI LEARNING\Json Files\+2 Commerce Course List.json"
    output_excel_file = "+2 Commerce Course List Spreadsheet.xlsx"
    json_to_excel(input_json_file, output_excel_file)
    print(f"Conversion completed. JSON file '{input_json_file}' has been converted to Excel file '{output_excel_file}'.")