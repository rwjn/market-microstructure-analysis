for key, df in t3_cleaned_data.items():
    # Initial block condition: Orders must be greater than 1
    initial_block_condition = (df['ask_quantity'] > 1) & (df['bid_quantity'] > 1)
    # Additional block conditions: At least 10x the counterparty size, and bigger than the previous order on its side of the LOB
    additional_block_condition = ((df['bid_quantity'] >= 10 * df['ask_quantity']) & (df['bid_quantity'] > df['bid_quantity'].shift(1))) | \
                                 ((df['ask_quantity'] >= 10 * df['bid_quantity']) & (df['ask_quantity'] > df['ask_quantity'].shift(1)))
    # Combined block order condition
    block_order_condition = initial_block_condition & additional_block_condition
    # Create 'block order' column with 1 if true, 0 otherwise
    # 0 by default
    df['block_order'] = 0 
    df.loc[block_order_condition, 'block_order'] = 1  
    # Mid price calculation 
    df['mid'] = (df['ask_price'] + df['bid_price'])/2
    # Micro price calculation 
    total_quantity = (df['ask_quantity'] + df['bid_quantity'])
    df['micro'] = (df['bid_price'] * df['ask_quantity'] + df['ask_price'] * df['bid_quantity']) / total_quantity
    # Take absolute value of spread, so we can compare
    df['mid_micro_spread'] = abs(df['mid'] - df['micro'])
    # Calculate the spread before the block order
    df['pre_block_spread'] = df['mid_micro_spread'].shift(1)
    # These might generate n/a values, so we replace with 0s
    df.fillna(0, inplace=True)
    # Update the dataframe in the original dictionary
    t3_cleaned_data[key] = df