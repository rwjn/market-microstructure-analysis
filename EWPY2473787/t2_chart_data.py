def chart_data(df):
    if df.empty:
        # If it is empty, we do not want an error, so replace with 0
        df.loc[0] = [0, 0, 0, 0] 
    # Replace np.nan values in the first row with 0
    df.iloc[0] = df.iloc[0].fillna(0)
    # Fill N/As in columns that contain 'quantity' in the column name with 0
    quantity_columns = [col for col in df.columns if 'quantity' in col]
    df[quantity_columns] = df[quantity_columns].fillna(0)
    # Fill forward columns that contain 'price' in their name
    price_columns = [col for col in df.columns if 'price' in col]
    df[price_columns] = df[price_columns].ffill()
    # We need it to be integers so we can calculate mid/micro price.
    df = df.astype(int)
    # Check if column empty, i.e. if user specifies 9 AM: 
    return df