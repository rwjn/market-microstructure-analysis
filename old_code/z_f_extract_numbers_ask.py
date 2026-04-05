# Import required libaries
import regex as re
import pandas as pd

def extract_numbers_ask(string):
    # Extract numbers from string. This will make a list.
    numbers = re.findall(r'\d+', string)
    ask_price = []
    ask_quantity = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            ask_price.append(numbers[i])
        else:
            ask_quantity.append(numbers[i])
    df_new = pd.DataFrame({'ask_price': ask_price, 
                           'ask_quantity': ask_quantity})
    
    return df_new