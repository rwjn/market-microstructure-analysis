# Using file dataframe, we can use user inputs on file type and dates to output the correct files as a list
def get_file_list(df, file_type_input, date_input, end_date_input):
    # Change case so its consistent with user input (also .lower), and match with file type choice.
    df_temp = df[df['lob_or_tapes'].str.lower() == file_type_input]

    # Reset, as we are dropping variables, we do not want an error
    df_temp.reset_index(drop=True, inplace=True)

    # Get index value of end date in dataframe
    end_index = df_temp.index[df_temp['date'] == end_date_input][0]
    # Get index value of start date in dataframe
    start_index = df_temp.index[df_temp['date'] == date_input][0]

    # Slice to take files within the date range
    file_list = df_temp['filename'].iloc[start_index:end_index + 1].tolist()

    return file_list