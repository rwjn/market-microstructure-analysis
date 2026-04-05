import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import os
import ast

# Function to output top bid/ask price & quantity from a string

def t3_func(lob):
    # Convert the string representation of list to an actual list
    # Use ast to safely convert 
    lob_list = ast.literal_eval(lob)
    try:    
        # Take the first list (i.e. the one that contains bids), the second list within it (ignoring the 'bid' marker) and then the first item in the bid list.
        bid_price, bid_quantity = lob_list[0][1][0]
    # If there are no bids at a price, we don't want an error
    except IndexError:
        bid_price, bid_quantity = 0, 0
    try:
        # Take the second list (i.e. the one that contains asks), the second list within it (ignoring the 'ask' marker) and then the first item in the ask list.
        ask_price, ask_quantity = lob_list[1][1][0]
    # If there are no asks at a price, we don't want an error. 
    except IndexError:
        ask_price, ask_quantity = 0, 0
    
    output = [bid_price, bid_quantity, ask_price, ask_quantity] 
    
    return output

# # Test:
# lob = "[['bid', [[335, 8], [334, 7], [331, 5], [328, 12], [324, 15], [321, 2], [308, 6], [305, 4], [301, 7]]], ['ask', [[339, 2], [344, 3], [348, 8]]]]"
# lob2 = "[['bid', [[0, 0], [334, 7], [331, 5], [328, 12], [324, 15], [321, 2], [308, 6], [305, 4], [301, 7]]], ['ask', [[0, 0], [344, 3], [348, 8]]]]"
# t3_func(lob2)

# Applies t3_func to a dataset

def t3_lob_files(file_list, time_col=1, lob_col=4):
    # Dictionary for processed dataframes
    processed_dfs = {}

    # Using Dave Cliff's format
    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Read dataframe
            df = pd.read_csv(fname, usecols=[time_col, lob_col], header=None)
            # Set column names
            df.columns = ['time', 'lob']
            # Apply the t3_func, and make each item in the list a row value 
            df[['bid_price', 'bid_quantity', 'ask_price', 'ask_quantity']] = df['lob'].apply(t3_func).tolist()
            # Drop LOB as we no longer need it
            df.drop('lob', axis=1, inplace=True)
            # Save DF with filename
            processed_dfs[fname] = df
            # Notify that file has been processed
            print(f"Processed {fname}")
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')

    return processed_dfs

