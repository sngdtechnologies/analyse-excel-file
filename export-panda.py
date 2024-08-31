import pandas as pd

# Load the Excel file with the .xlsb format
file_path = '/path.xlsb'
xls = pd.read_excel(file_path, sheet_name=None, engine='pyxlsb')

# Get the sheet names and print a summary of each sheet
sheet_summary = {sheet: xls[sheet].head() for sheet in xls.keys()}
sheet_summary
