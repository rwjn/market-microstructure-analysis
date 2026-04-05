### For User Output ### 
# We require the following  libraries

# Regex to find numbers
import re
# Datetime for time processing
from datetime import datetime
# As we are using dataframes
import pandas as pd
# As we need to know where to export
import os
# To assign N/A value
import numpy as np

# Our custom function:
from t1_functions import find_time


# Function 4: Verbatim Tape Files
# Inputs of file list, start/end times, export choice (no as default), export directory.
def vb_tape_files(file_list, start_time_seconds, end_time_seconds, export_choice="no", output_dir = "", time_col=2,):
    # Dictionary to store processed dataframes
    processed_dfs = {}
    # For loop in selected files
    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Read and process the dataframe
            df = pd.read_csv(fname, header = None)
            # If the file is the first in the list, use the specified start time.
            if fname == file_list[0]:
                df = df[df[time_col] >= start_time_seconds]
            # If the file is the last in the list, take data before specified end time.
            if fname == file_list[-1]:
                df = df[df[time_col] <= end_time_seconds]
            
            # Store the processed dataframe, same name as before
            processed_dfs[fname] = df
            
            # Export to CSV if export_choice is 'yes'
            if export_choice.lower() == "yes":
                # Add string to start of fname to differentiate it from input files.
                output_fname = 'VB_Output_' + fname
                # Use output directory specified by user name, joined to file name.
                output_filename = os.path.join(output_dir, output_fname)
                # Export as CSV
                df.to_csv(output_filename, index=False, header = None)
                # Inform user of progress
                print(f'Exported {fname} as {output_filename}')
        else:
            # If we encounter a non-CSV file
            print(f'FAIL: File with extension={extension} can\'t be handled')

    return processed_dfs

# Function 5: For Summary LOB Files

def process_tape_files(file_list, start_time_seconds, end_time_seconds, export_choice = "no", output_dir = "", trade_col = 0, time_col = 2):
    
    # Works to save a list, appending after each file, which updates a main dataframe
    data = []
    # Change DC's code - we do not need to specify
    header_len = len('UoB_Set01_')
    # Loop through specified LOB files
    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Get date from filename
            date_str = fname[header_len:header_len+10]
            # Only use columns we need.
            df = pd.read_csv(fname, usecols=[trade_col, time_col])
            df.columns = ['tape', 'time']
            # If file name is the same as start date:
            if fname == file_list[0]:
                # Then only take rows after the start time
                df = df[df['time'] >= start_time_seconds]
            # If file name is the same as the end date:
            if fname == file_list[-1]:
                # Then only take rows before the end
                df = df[df['time'] <= end_time_seconds]
            # We no longer need 'time' variable, so drop
            df.drop('time', axis =1, inplace = True)
            # Count number of cancelled orders
            count_can = df['tape'].str.count('CAN').sum()
            # Count number of trades
            count_trade = df['tape'].str.count('TRADE').sum()
            # Append list with each new file result
            data.append([date_str, count_can, count_trade])
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')
    # Save result dataframe
    result_df = pd.DataFrame(data, columns=['Date', '# of CAN', '# of Trades']) 
    # Exporting
    if export_choice.lower() == "yes":
        # Join with filename to create full path
        output_filename = os.path.join(output_dir, 'processed_tape_data.csv')
        # Export
        result_df.to_csv(output_filename, index=False)
        # Notify user that export has happened
        print(f'DataFrame exported as {output_filename}')
    return result_df

# Function 6: Verbatim LOB Files

def vb_lob_files(file_list, start_time_seconds, end_time_seconds, export_choice = "no", output_dir = "",time_col = 1):
    # Dictionary to store processed dataframes
    processed_dfs = {}
    # Work through all files in specified date range.
    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Read file data
            df = pd.read_csv(fname, header = None)
            # If file name is the same as start date:
            if fname == file_list[0]:
                # Then only take rows after the start time.
                df = df[df[time_col] >= start_time_seconds]
            # If file name is the same as the end date:
            if fname == file_list[-1]:
                # Then only take rows before the end.
                df = df[df[time_col] <= end_time_seconds]
            # Add processed df to dictionary 
            processed_dfs[fname] = df
            # Export to CSV if export_choice is 'yes'
            if export_choice.lower() == "yes":
                # Add string to start of fname to differentiate it from input files.
                output_fname = 'VB_Output_' + fname
                output_filename = os.path.join(output_dir, output_fname)
                df.to_csv(output_filename, index=False, header = None)
                print(f'Exported {fname} as {output_filename}')
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')

    return processed_dfs
 
# Function 7: LOB OHLC

def process_lob_files(file_list, start_time_seconds, end_time_seconds, export_choice = "no", output_dir = "", price_col = 3, time_col = 1):
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
