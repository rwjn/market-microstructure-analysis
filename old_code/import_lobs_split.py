import pandas as pd   

import regex as re

from datetime import datetime

import os

import numpy as np

def process_lob_files(header_string, file_list, start_time_seconds, end_time_seconds, lob_col = 4, time_col = 1):

    data = []
    header_len = len(header_string)

    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            df = pd.read_csv(fname, usecols=[time_col, lob_col])
            df.columns = ['time', 'lob']
            df = df[df['time'] > start_time_seconds]
            df = df[df['time'] < end_time_seconds]
            # df[['bid', 'ask']] = df['lob'].apply(split_lob).apply(pd.Series)
            # df.drop('lob', axis =1, inplace = True)
            data.append()
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')
    return pd.DataFrame(data, columns=['time', 'lob'])

os.chdir("/Users/robertnoble/Library/CloudStorage/OneDrive-UniversityofBristol/EWDS/EWPY/Assessment/DataSet01")

file_list_ = ['UoB_Set01_2024-01-02LOBs.csv']
start_time_seconds = 0
end_time_seconds = 5
result_df = process_lob_files('UoB_Set01_', file_list_, start_time_seconds, end_time_seconds)
result_df
