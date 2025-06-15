import pandas as pd


excel_file = pd.ExcelFile('/mnt/processed_data.xlsx')

sheet_names = excel_file.sheet_names
sheet_names