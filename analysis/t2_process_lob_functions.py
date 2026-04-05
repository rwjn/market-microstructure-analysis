# Import libraries

# Pandas for dataframes
import pandas as pd
# Our custom functions to extract relevant numbers:
from t2_functions import extract_numbers_ask
from t2_functions import extract_numbers_bid
from f_split_lob import split_lob

# Function 1: Process LOBs for Graph 1

# Specify function, unlike for G2, file list will just be a single file, we don't have a start and end time, just a single value
def g1_process_lobs(file_list, g1_time_seconds, time_col = 1, lob_col = 4):
    # By default we assumme that the specified time is in the file
    nearest_time = False
    # As this is for chart 1, assume there's only one file and one specific time
    file = file_list[0]
    # Read the current file into a DataFrame
    df = pd.read_csv(file, usecols=[time_col, lob_col], header = None)
    # Specify column names, using function parameters
    df.columns = ['time', 'lob']
    # If the user specifies a time, and there is not an exact match, take the nearest time
    if not df['time'].isin([g1_time_seconds]).any():
        nearest_time = True
        # Sort the absolute differences between every time and the specified time, and take the closest absolute value
        df = df.iloc[(df['time'] - g1_time_seconds).abs().argsort()[:1]]
        # Save time used as DF name
        df_name = df['time'].iloc[0]
        # Notify yser
        print(f"There was no new LOB file produced at {g1_time_seconds} seconds after 9 AM. Taking the nearest time: {df_name}")
    # If there is an exact match
    if not nearest_time:
        # Set DF to this time
        df = df[df['time'] == g1_time_seconds]
        # Again, set the name as the time used
        df_name = g1_time_seconds
    # Apply our split function to the 'lob' column, separating bid and ask.
    df[['bid', 'ask']] = df['lob'].apply(split_lob).apply(pd.Series)
    # Remove 'lob' column - no longer needed as we now have bid and ask column    
    df.drop('lob', axis =1, inplace = True)
    # Iterate through each row in the DataFrame. Not necessarily needed for graph 1, but works well with my extract_ functions.
    for index, row in df.iterrows():
        # Using my custom function, create a dataset of bid prices/quantities, using all of the numbers in the bid column.
        bid_df = extract_numbers_bid(row['bid']).reset_index(drop=True)
        # Using my custom function, create a dataset of ask prices/quantities, using all of the numbers in the ask column.
        ask_df = extract_numbers_ask(row['ask']).reset_index(drop=True)
        # Merge bid and ask DataFrames side by side
        df = pd.concat([bid_df, ask_df], axis=1)
        # Set DF name
        df.name = df_name
    # Print to notify user
    print(f"LOB file at {df_name} seconds after 9 AM.")
    return df

# Function 2: Process LOBs for Graph 2

def g2_process_lobs(file_list, start_time_seconds, end_time_seconds, time_col = 1, lob_col = 4):
    # Dictionary to store all the DataFrames
    dataframes = {}
    # Iterate through each file in the file list
    for file in file_list:
        # Read the current file into a DataFrame
        df = pd.read_csv(file, usecols=[time_col, lob_col], header = None)
        df.columns = ['time', 'lob']
        # If we are using start date file
        if file == file_list[0]:
                if start_time_seconds == 0:
                    # Remove those with no values
                    df = df[df['time'] > start_time_seconds]
                else:
                     df = df[df['time'] >= start_time_seconds]
            # If file name is the same as the end date
        if file == file_list[-1]:
                # Then only take rows before the end
                df = df[df['time'] <= end_time_seconds]
        # Split lob into bid and ask columns
        df[['bid', 'ask']] = df['lob'].apply(split_lob).apply(pd.Series)
        # We no longer need 'lob' column, so drop
        df.drop('lob', axis =1, inplace = True)
        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            # Apply our custom functions to every row
            bid_df = extract_numbers_bid(row['bid']).reset_index(drop=True)
            ask_df = extract_numbers_ask(row['ask']).reset_index(drop=True)
            # Save name as the time value for that row
            df_name_lob = (row['time'])
            # Concatenate bid and ask DataFrames side by side
            dataframes[df_name_lob] = pd.concat([bid_df, ask_df], axis=1)
    return dataframes

