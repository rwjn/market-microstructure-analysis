import pandas as pd
from f_extract_numbers_ask import extract_numbers_ask
from f_extract_numbers_bid import extract_numbers_bid
from f_split_lob import split_lob
 
def process_lobs(file_list, start_time_seconds, end_time_seconds, time_col = 1, lob_col = 4):
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

        df[['bid', 'ask']] = df['lob'].apply(split_lob).apply(pd.Series)
        
        df.drop('lob', axis =1, inplace = True)

        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            bid_df = extract_numbers_bid(row['bid']).reset_index(drop=True)
            ask_df = extract_numbers_ask(row['ask']).reset_index(drop=True)

            df_name_lob = (row['time'])

            # Concatenate bid and ask DataFrames side by side
            dataframes[df_name_lob] = pd.concat([bid_df, ask_df], axis=1)

    return dataframes
