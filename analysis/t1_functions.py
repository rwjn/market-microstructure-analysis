# Regex to find numbers
import re
# Datetime for time processing
from datetime import datetime

# Function 1: Find Date
# Can be used for strings (i.e. file list & user input)

def find_date(file):
    # Extract patterns that match this format - 4 numbers - 2 numbers - 2 numbers
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', file) 
    try:
        # Select the match date
        date = date_match.group(0)
        # See if the match date is a valid date using datetime strptime
        datetime.strptime(date, '%Y-%m-%d')
        # Output just date
        return date
    except (ValueError, AttributeError):
        # If there is an error we do not want it to crash, return False to restart loops
        return False
    
# Function 2: Get correct file list 
    
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
    # Output list
    return file_list

# Function 3: Find Time

def find_time(input_time):
    try:
        # If the user does not specify decimal places
        if len(input_time) == 8:
            # Extract time that matches our expected format: HH:MM:SS
            time_match = re.search(r'\d{2}:\d{2}:\d{2}', input_time) 
            # Assume on the second if no ms specified
            ms = '.000'
            time = time_match.group(0)
            # Add miliseconds, so we can use both 3 DP and no DP
            time = time + ms
            # Take time in datetime format
            datetime.strptime(time, '%H:%M:%S.%f')
        else:
            # If 3 DP are specified
            time_match = re.search(r'\d{2}:\d{2}:\d{2}.\d{3}', input_time) 
            time = time_match.group(0)
            # Take time in datetime format
            datetime.strptime(time, '%H:%M:%S.%f')
        return time
    # If it is not a valid time or not the right length it will not crash
    except (ValueError, AttributeError):
        return False
    