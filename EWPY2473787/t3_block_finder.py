# Function to identify block orders in our CSV file
def t3_block_finder(t3_cleaned_data):
    # Setup empty dictionary
    block_data = {}
    # Loop through each pair in our dictionary
    for key, df in t3_cleaned_data.items():
        # Our order sizes must be greater than 1
        df = df[(df['ask_quantity'] > 1) & (df['bid_quantity'] > 1)]
        # Our other conditions, that it must be at least 10x the counterparty size, and bigger than the previous order on its side of the LOB.
        df = df[((df['bid_quantity'] >= 10 * df['ask_quantity']) & (df['bid_quantity'] > df['bid_quantity'].shift(1))) |
                ((df['ask_quantity'] >= 10 * df['bid_quantity']) & (df['ask_quantity'] > df['ask_quantity'].shift(1)))]
        # Save block dataframes, with the name the same as before
        block_data[key] = df
    # Output our new dictionary
    return block_data