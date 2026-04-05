
# This file uses Dave Cliffs 'OHLC.py' file, but as a function.
# In the .ipynb, user will specify chosen files with inputs 'file_list'.
# The user will also specify start and end times


import pandas as pd   

import regex as re

from datetime import datetime

import os

import numpy as np

def process_lob_files(file_list, start_time_seconds, end_time_seconds, export_choice = "no", output_dir = "", price_col = 3, time_col = 1):
    
    # Processes a list of CSV files and prints a summary of the prices.

    # Required arguments:
    # header_string (str): The session-id header string on the files to process.
    # file_list (list): List of filenames to be processed. Specified in ipynb file from start/end date input.
    # start_time_seconds: From user input of start time, converted to seconds after 9 AM.
    # end_time_seconds: From user input of end time, converted to seconds after 9 AM.
    # price_col (int): Column index for the mid-price in the CSV files.
    # time_col (int): Column index for time after 9 AM (seconds)

    # Returns:
    # DataFrame: A DataFrame containing the date, open, high, low, and close prices.
    

    data = []
    header_len = len('UoB_Set01_')

    for fname in file_list:
        
        extension = fname[-4:]
        if extension == '.csv':
            # Get date from filename
            date_str = fname[header_len:header_len+10]
            df = pd.read_csv(fname, usecols=[time_col, price_col], header = None)
            df.columns = ['time', 'price']
            # If file name is the same as start date:
            if fname == file_list[0]:
                # Then only take rows after the start time.
                df = df[df['time'] >= start_time_seconds]
            # If file name is the same as the end date:
            if fname == file_list[-1]:
                # Then only take rows before the end.
                df = df[df['time'] <= end_time_seconds]
            # We no longer need 'time' variable, so drop.
            df.drop('time', axis =1, inplace = True)
            # Remove rows where price is -1. However, if only -1 in time period, we don't an error, so we will replace with N/A later.
            if df['price'].iloc[-1] != -1:
                df = df[df['price'] != -1]
            price_open = df['price'].iloc[0]
            price_high = df['price'].max()
            price_low = df['price'].min()
            price_close = df['price'].iloc[-1]
            data.append([date_str, price_open, price_high, price_low, price_close])
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')
    
    # Call required data, replace any '-1' values with NA, should only happen if we look at a period before a mid-price.
    result_df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close']).replace(-1, np.NaN) 

    if export_choice.lower() == "yes":
        # Join with filename to create full path
        output_filename = os.path.join(output_dir, 'processed_lob_ohlc_data.csv')
        # Export
        result_df.to_csv(output_filename, index=False)
        # Notify user that export has happened
        print(f'DataFrame exported as {output_filename}')
    
    return result_df

# file_list = ['UoB_Set01_2024-01-02LOBs.csv'] # Replace with actual file names
# start_time_seconds = 0
# end_time_seconds = 5
# result_df = process_lob_files('UoB_Set01_', file_list, start_time_seconds, end_time_seconds)
# result_df
