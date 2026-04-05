# Code to get user input for start time. Run from ipynb file.

# Use 'while' loop so that user is continuously prompted.
while True:
    # Ask user to input in certain form.
    date_input_raw = input("Please enter your start date in the format 'MM-DD'. The time frame is 01-02 (2024) to 06-28 (2024):").strip()
    # Change to format to match files, and to work with find_date() function
    date_input = '2024-' + date_input_raw 
    if date_input_raw == '':
        print("You have not entered a start date.")
        # Break so that user can escape, if 'esc' pressed.
        break
    # If the input is not in the correct format, checks with find_date format.
    elif find_date(date_input) == False:
        print(f"'{date_input_raw}' is not a valid date. Please use 'MM-DD'.")
    # See if it is too many characters
    elif len(date_input_raw) != 5:
        print(f"{date_input_raw} is too long. Please use 'MM-DD'")
    # See if it is within the specified dates.
    elif date_input > file_list['date'].iloc[-1]:
        print(f"Error. {date_input_raw} is after the latest date of 06-28. Please enter another date")
    elif date_input not in file_list['date'].values:
        print(f"{date_input} is not a working day. Please enter another date.")
    else:
        filename_start = file_list.loc[file_list['date'] == date_input, 'filename'].values[0]
        print(f"You have chosen {date_input} as your start date.")
        while True:
            end_date_input_raw = input("Please enter your end date in the format 'MM-DD'. The time frame is 01-02 (2024) to 06-28 (2024):").strip()
            end_date_input = '2024-' + end_date_input_raw 
            if end_date_input_raw == '':
                print("You have not entered an end date.")
                # Break so that user can escape, if 'esc' pressed.
                break
            elif find_date(end_date_input) == False:
                print(f"'{end_date_input_raw}' is not a valid date. Please use 'MM-DD'.")
            # See if it is too many characters
            elif len(end_date_input_raw) != 5:
                print(f"{end_date_input_raw} is too long. Please use 'MM-DD'")
            # See if it is within the specified dates.
            elif end_date_input > file_list['date'].iloc[-1]:
                print(f"Error. {end_date_input_raw} is after the latest date of 06-28. Please enter another date.")
            elif end_date_input not in file_list['date'].values:
                print(f"{end_date_input} is not a working day. Please enter another date.")
            # Use index to see if start date comes after end date, and raise an error if so
            elif file_list.index[file_list['date'] == date_input][0] > file_list.index[file_list['date'] == end_date_input][0]:
                print(f"End date ({end_date_input}) cannot be before start date ({date_input}). Please enter another end-date.")
            else:
                filename_end = file_list.loc[file_list['date'] == end_date_input, 'filename'].values[0]
                print(f"You have chosen {end_date_input} as your end date.")
                break
        break

