
# First we make an empty list to store the results
result = []

# Go through each df in block_data dictionary
for filename, df in block_data.items():
    # Get the number of rows in the dataframe
    num_observations = len(df)
    # Add the filename and number of rows to the result list
    result.append({'filename': filename, 'number of observations': num_observations})

# Create a dataframe from the result list
result_df = pd.DataFrame(result)

