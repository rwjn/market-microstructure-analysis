# Import required libaries
import regex as re
import pandas as pd

def extract_numbers_bid(string):
    # Extract numbers from string. This will make a list.
    numbers = re.findall(r'\d+', string)
    bid_price = []
    bid_quantity = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            bid_price.append(int(numbers[i]))
        else:
            bid_quantity.append(int(numbers[i]))
    df_new = pd.DataFrame({'bid_price': bid_price, 
                           'bid_quantity': bid_quantity})
    return df_new

