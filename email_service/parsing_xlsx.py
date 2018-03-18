import pandas as pd
from parsing_CSV_function import parsing_csv

def parsing_xlsx(file_path):
    data_xls = pd.read_excel(file_path, index_col=None)
    data_xls.to_csv('created.csv', encoding='utf-8',index=False)

    return parsing_csv('created.csv')





