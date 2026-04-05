import numpy as np

# Function to calculate mid price
def calculate_mid_price(bid_price, ask_price):
    if len(bid_price) == 0 or len(ask_price) == 0:
        return np.nan
    elif bid_price == 0 and ask_price == 0:
        return np.nan
    else:
        return (max(bid_price) + min(ask_price)) / 2

def calculate_micro_price(bid_price, bid_quantity, ask_price, ask_quantity):
    if len(bid_price) == 0 or len(ask_price) == 0:
        return np.nan
    # As the highest bid and ask are top of the columns
    total_quantity = bid_quantity[0] + ask_quantity[0]
    try: 
        micro_price = (bid_price[0] * ask_quantity[0] + ask_price[0] * bid_quantity[0])/total_quantity
    # If we have set the row as 0s for the chart to work, we do not want an error here
    except ZeroDivisionError:
        micro_price = np.nan
    return micro_price 