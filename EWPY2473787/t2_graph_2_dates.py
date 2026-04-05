# Code to get user input for Chart 2 dates. Run from ipynb file.
# While loop, with nested while loop.

# Use 'while' loop so that user is continuously prompted.

### Start Date ###
while True:
    old_date_choice = input("Would you like to use your specified start or end dates from Task 1 for Chart 2's start date? Enter 'start' for previous start date, 'end' for previous end date, or 'new' to specify a new date.").strip().lower()
    old_date_choice_list = ['start', 'end', 'new']
    if old_date_choice == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    elif old_date_choice not in old_date_choice_list:
        print(f"'{old_date_choice}' not recognised. Please enter 'start', 'end' or 'new'.")
    elif old_date_choice == "start":
        g2_date_input = date_input
        g2_filename = file_list.loc[file_list['date'] == g2_date_input, 'filename'].values[0]
        print(f"You have chosen {g2_date_input} as your Chart 2 start date.")
        break
    elif old_date_choice == "end":
        g2_date_input = end_date_input
        g2_filename = file_list.loc[file_list['date'] == g2_date_input, 'filename'].values[0]
        print(f"You have chosen {g2_date_input} as your Chart 2 start date.")
        break
    else:
        print("You have chosen to select a new date.")
        # If the user wants a new date...
        while True:
            # Ask user to input in certain form.
            g2_date_input_raw = input("Please enter a new start date to extract LOB data in the format 'MM-DD' for Chart 2. The time frame is 01-02 (2024) to 06-28 (2024):").strip()
            # Change to format to match files, and to work with find_date() function
            g2_date_input = '2024-' + g2_date_input_raw 
            if g2_date_input_raw == '':
                print("You have not entered a value.")
                # Break so that user can escape, if 'esc' pressed.
                break
            # If the input is not in the correct format, checks with find_date format.
            elif find_date(g2_date_input) == False:
                print(f"'{g2_date_input_raw}' is not a valid date. Please use 'MM-DD'.")
            # See if it is too many characters
            elif len(g2_date_input_raw) != 5:
                print(f"{g2_date_input_raw} is incorrect length. Please use 'MM-DD'")
            # See if it is within the specified dates.
            elif g2_date_input > file_list['date'].iloc[-1]:
                print(f"Error. {g2_date_input_raw} is after the latest date of 06-28. Please enter another date")
            elif g2_date_input not in file_list['date'].values:
                print(f"{g2_date_input} is not a working day. Please enter another date.")
            else:
                g2_filename = file_list.loc[file_list['date'] == g2_date_input, 'filename'].values[0]
                print(f"You have chosen {g2_date_input} as your Chart 2 start date.")
                break
        break

### End Date ###
    
while True:
    old_date_choice = input("Would you like to use your specified start or end dates from Task 1 for Chart 2's end date? Enter 'start' for previous start date, 'end' for previous end date, or 'new' to specify a new date. It is highly recommended start and dates are the same.").strip().lower()
    old_date_choice_list = ['start', 'end', 'new']
    if old_date_choice == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    elif old_date_choice not in old_date_choice_list:
        print(f"'{old_date_choice}' not recognised. Please enter 'start', 'end' or 'new'.")
    elif old_date_choice == "start":
        g2_end_date_input = date_input
        g2_end_filename = file_list.loc[file_list['date'] == g2_end_date_input, 'filename'].values[0]
        if file_list.index[file_list['date'] == g2_date_input][0] > file_list.index[file_list['date'] == g2_end_date_input][0]:
        # Use index to see if start date comes after end date, and raise an error if so
            print(f"End date ({g2_end_date_input}) cannot be before start date ({g2_date_input}). Please enter another end-date.")
        else:
            print(f"You have chosen {g2_end_date_input} as your Chart 2 end date.")
            break
    elif old_date_choice == "end":
        g2_end_date_input = end_date_input
        g2_end_filename = file_list.loc[file_list['date'] == g2_end_date_input, 'filename'].values[0]
        if file_list.index[file_list['date'] == g2_date_input][0] > file_list.index[file_list['date'] == g2_end_date_input][0]:
        # Use index to see if start date comes after end date, and raise an error if so
            print(f"End date ({g2_end_date_input}) cannot be before start date ({g2_date_input}). Please enter another end-date.")
        else:
            print(f"You have chosen {g2_end_date_input} as your Chart 2 end date.")
            break
    else:
        print("You have chosen to select a new date.")
        # If the user wants a new date...
        while True:
            # Ask user to input in certain form.
            g2_end_date_input_raw = input("Please enter a new end date to extract LOB data in the format 'MM-DD' for Chart 2. The time frame is 01-02 (2024) to 06-28 (2024):").strip()
            # Change to format to match files, and to work with find_date() function
            g2_end_date_input = '2024-' + g2_end_date_input_raw 
            if g2_end_date_input_raw == '':
                print("You have not entered a value.")
                # Break so that user can escape, if 'esc' pressed.
                break
            # If the input is not in the correct format, checks with find_date format.
            elif find_date(g2_end_date_input) == False:
                print(f"'{g2_end_date_input_raw}' is not a valid date. Please use 'MM-DD'.")
            # See if it is too many characters
            elif len(g2_end_date_input_raw) != 5:
                print(f"{g2_end_date_input_raw} is incorrect length. Please use 'MM-DD'")
            # See if it is within the specified dates.
            elif g2_end_date_input > file_list['date'].iloc[-1]:
                print(f"Error. {g2_end_date_input_raw} is after the latest date of 06-28. Please enter another date")
            elif g2_end_date_input not in file_list['date'].values:
                print(f"{g2_end_date_input} is not a working day. Please enter another date.")
            elif file_list.index[file_list['date'] == g2_date_input][0] > file_list.index[file_list['date'] == g2_end_date_input][0]:
            # Use index to see if start date comes after end date, and raise an error if so
                print(f"End date ({g2_end_date_input}) cannot be before start date ({g2_date_input}). Please enter another end-date.")
            else:
                g2_end_filename = file_list.loc[file_list['date'] == g2_end_date_input, 'filename'].values[0]
                print(f"You have chosen {g2_end_date_input} as your Chart 2 end date.")
                break
        break

# As in task 1, we will now use our custom function to print the file we have selected
g2_selected_files = get_file_list(file_list, 'lob', g2_date_input, g2_end_date_input)
print(f"You have selected: {g2_selected_files}")

# Warning if dates are not the same:
if g2_date_input != g2_end_date_input:
    print("Warning, to avoid crashing it is highly recommended you select a short time period (<2 minutes)")
