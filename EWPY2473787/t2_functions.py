# Import libaries
# To find numbers:
import regex as re
# For dataframes
import pandas as pd
# To assign N/A values
import numpy as np

# Function 1: Split 'lob' column into two

def split_lob(lob):
    try:
        # The ']],' separates the bid and ask in the lob column
        bid, ask = lob.split(']],')
    # Avoid crashing
    except ValueError:
        return lob, lob
    # Will return as 2 separate DF columns
    return bid, ask

# Function 2: Extract 'bid' quantities and prices

def extract_numbers_bid(string):
    # Extract numbers from string to make a list of all numbers
    numbers = re.findall(r'\d+', string)
    # Create empty bid price list
    bid_price = []
    # Create empty bid quantity list
    bid_quantity = []
    # We can use the list of numbers, and because price/quantity alternate, assign each one to the correct list
    for i in range(len(numbers)):
        # As the first [0th] position will be price, we can assume its index is even
        if i % 2 == 0:
            # Add to price list
            bid_price.append(int(numbers[i]))
        else:
            # Otherwise add to quantity list
            bid_quantity.append(int(numbers[i]))
    # Create a dataframe which combines these two lists
    df_new = pd.DataFrame({'bid_price': bid_price, 
                           'bid_quantity': bid_quantity})
    return df_new

# Function 3: Extract 'ask' quantities and prices

def extract_numbers_ask(string):
    # Extract numbers from string, making a list
    numbers = re.findall(r'\d+', string)
    # Again, we will create two empty lists, to fill with prices and quantities
    ask_price = []
    ask_quantity = []
    # Again, use the fact that all prices will have an even index position
    for i in range(len(numbers)):
        if i % 2 == 0:
            ask_price.append(numbers[i])
        else:
            ask_quantity.append(numbers[i])
    # Create a new dataframe for ask prices/quantities
    df_new = pd.DataFrame({'ask_price': ask_price, 
                           'ask_quantity': ask_quantity})
    return df_new

# Function 4: Calculate mid price (arithmetic mean of two highest)

def calculate_mid_price(bid_price, ask_price):
    # If either are empty we cannot calculate the mid-price, return N/A
    if len(bid_price) == 0 or len(ask_price) == 0:
        return np.nan
    # Otherwise, take the highest bid and lowest ask and divide by 2
    return (max(bid_price) + min(ask_price)) / 2

# Function 5: Calculate ask price

def calculate_micro_price(bid_price, bid_quantity, ask_price, ask_quantity):
    # Again, if either are empty we cannot calculate
    if len(bid_price) == 0 or len(ask_price) == 0:
        return np.nan
    # As the highest bid and ask are top of the columns, we can use the [0] position
    total_quantity = bid_quantity[0] + ask_quantity[0]
    # Use micro price formula
    return (bid_price[0] * ask_quantity[0] + ask_price[0] * bid_quantity[0])/total_quantity

