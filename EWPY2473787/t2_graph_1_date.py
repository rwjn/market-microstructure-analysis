# Code to get user input for Chart 1 time. Run from ipynb file.
# While loop, with nested while loop.

# Use 'while' loop so that user is continuously prompted.
while True:
    old_date_choice = input("For Chart 1, would you like to use your specified start or end dates from Task 1? Enter 'start' for previous start date, 'end' for previous end date, or 'new' to specify a new date.").strip().lower()
    old_date_choice_list = ['start', 'end', 'new']
    if old_date_choice == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    elif old_date_choice not in old_date_choice_list:
        print(f"'{old_date_choice}' not recognised. Please enter 'start', 'end' or 'new'.")
    elif old_date_choice == "start":
        g1_date_input = date_input
        g1_filename = file_list.loc[file_list['date'] == g1_date_input, 'filename'].values[0]
        print(f"You have chosen {g1_date_input} as your Chart 1 date.")
        break
    elif old_date_choice == "end":
        g1_date_input = end_date_input
        g1_filename = file_list.loc[file_list['date'] == g1_date_input, 'filename'].values[0]
        print(f"You have chosen {g1_date_input} as your Chart 1 date.")
        break
    else:
        print("You have chosen to select a new date.")
        # If the user wants a new date...
        while True:
            # Ask user to input in certain form.
            g1_date_input_raw = input("Please enter a new date to extract LOB data in the format 'MM-DD' for Chart 1. The time frame is 01-02 (2024) to 06-28 (2024):").strip()
            # Change to format to match files, and to work with find_date() function
            g1_date_input = '2024-' + g1_date_input_raw 
            if g1_date_input_raw == '':
                print("You have not entered a value.")
                # Break so that user can escape, if 'esc' pressed.
                break
            # If the input is not in the correct format, checks with find_date format.
            elif find_date(g1_date_input) == False:
                print(f"'{g1_date_input_raw}' is not a valid date. Please use 'MM-DD'.")
            # See if it is too many characters
            elif len(g1_date_input_raw) != 5:
                print(f"{g1_date_input_raw} is incorrect length. Please use 'MM-DD'")
            # See if it is within the specified dates.
            elif g1_date_input > file_list['date'].iloc[-1]:
                print(f"Error. {g1_date_input_raw} is after the latest date of 06-28. Please enter another date")
            elif g1_date_input not in file_list['date'].values:
                print(f"{g1_date_input} is not a working day. Please enter another date.")
            else:
                g1_filename = file_list.loc[file_list['date'] == g1_date_input, 'filename'].values[0]
                print(f"You have chosen {g1_date_input} as your Chart 1 date.")
                break
        break

