
# This file uses Dave Cliffs 'OHLC.py' file, but as a function.
# In the .ipynb, user will specify chosen files with inputs 'file_list'.
# The user will also specify start and end times


import pandas as pd   

import regex as re

from datetime import datetime

import os

def process_tape_files(file_list, start_time_seconds, end_time_seconds, export_choice = "no", output_dir = "", trade_col = 0, time_col = 2):
    

    data = []
    header_len = len('UoB_Set01_')

    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Get date from filename
            date_str = fname[header_len:header_len+10]
            df = pd.read_csv(fname, usecols=[trade_col, time_col])
            df.columns = ['tape', 'time']
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
            
            count_can = df['tape'].str.count('CAN').sum()
            count_trade = df['tape'].str.count('TRADE').sum()
            data.append([date_str, count_can, count_trade])
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')
        

    result_df = pd.DataFrame(data, columns=['Date', '# of CAN', '# of Trades']) 

    if export_choice.lower() == "yes":
        # Join with filename to create full path
        output_filename = os.path.join(output_dir, 'processed_tape_data.csv')
        # Export
        result_df.to_csv(output_filename, index=False)
        # Notify user that export has happened
        print(f'DataFrame exported as {output_filename}')

    return result_df


# To test:

# file_list = ['UoB_Set01_2024-01-02tapes.csv', 'UoB_Set01_2024-01-03tapes.csv'] 
# start_time_seconds = 0
# end_time_seconds = 5
# result_df = process_tape_files(file_list, start_time_seconds, end_time_seconds)
# result_df
