# Blank dictionary we will use for our times
block_times = {}

for key, df in t3_cleaned_data.items():
    # Only look at block orders
    # Loop to find start and end rows
    for i in df[df['block_order'] == 1].index:
        # We take time variable
        start_time = df.loc[i, 'time']
        # Take spread variable
        block_spread = df.loc[i, 'pre_block_spread']
        # Set up column in row where block occurs
        df.loc[i, 'seconds_after_block'] = df['time'].iloc[-1] - start_time
        # For rest of rows after start
        for j in range(i + 1, len(df)):
            # Check if the spread is greater than the pre-block spread, end if so
            if df.loc[j, 'mid_micro_spread'] <= block_spread:
                # Take time column
                end_time = df.loc[j, 'time']
                # Reset seconds after block variable
                df.loc[i, 'seconds_after_block'] = end_time - start_time
                # Find counterparty price change at the end
                counterparty_price = df.loc[j, 'ask_price'] if df.loc[i, 'ask_quantity'] < df.loc[i, 'bid_quantity'] else df.loc[j, 'bid_price']
                # Put in relevant row
                df.loc[i, 'counterparty_price'] = counterparty_price
                break

    # Calculate counterparty price change. As this is conditional we will use np.where
    df['counterparty_price_change'] = np.where(
        df['bid_quantity'] < df['ask_quantity'],
        abs(df['bid_price'] - df['counterparty_price']),
        abs(df['ask_price'] - df['counterparty_price'])
    )

    # Specify quantity size of block order
    df['block_order_size'] = np.where(
        df['bid_quantity'] < df['ask_quantity'],
        df['ask_quantity'],
        df['bid_quantity'])
    
    # Specify counter party order size
    df['cp_order_size'] = np.where(
        df['bid_quantity'] > df['ask_quantity'],
        df['ask_quantity'],
        df['bid_quantity'])
    
    # Specify counter party price
    df['cp_initial_price'] = np.where(
        df['bid_quantity'] > df['ask_quantity'],
        df['ask_price'],
        df['bid_price'])


    # Extract the rows where 'block_order' is 1 and there is a valid 'seconds_after_block'
    block_times[key] = df[(df['block_order'] == 1)].copy()
