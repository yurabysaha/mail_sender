import pandas as pd
from .parsing_CSV_function import parsing_csv


def parsing_xlsx(file_path, title):
    data_xls = pd.read_excel(title, index_col=None)
    data_xls.to_csv('/Users/viktorgrigorevskiy/Desktop/projects/mail_sender/media/{}.csv'.format(file_name), encoding='utf-8',index=False)

    return parsing_csv('media/{}.csv'.format(title))
