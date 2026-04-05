opening_time = datetime.strptime('09:00:00.000', '%H:%M:%S.%f')
closing_time = datetime.strptime('17:30:00.000', '%H:%M:%S.%f')

# Again, here we use a nested 'while' loop.

while True:
    # Option to use a new time or old ones
    old_time_choice = input("For Chart 1, would you like to use your specified start or end times from Task 1? Enter 'start' for previous start time, 'end' for previous end time, or 'new' to specify a new time.").strip().lower()
    # Possible choices
    old_time_choice_list = ['start', 'end', 'new']
    # Escape option
    if old_time_choice == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    # If unrecognised input
    elif old_time_choice not in old_time_choice_list:
        print(f"'{old_time_choice}' not recognised. Please enter 'start', 'end' or 'new'.")
    # If start - set time as 'start_time', specified earlier
    elif old_time_choice == "start":
        g1_time = start_time
        g1_time_seconds = (datetime.strptime(g1_time, '%H:%M:%S.%f') - opening_time).total_seconds()
        print(f"You have chosen {g1_time} as your Chart 1 time.")
        print(f"{g1_time_seconds} seconds after 9 AM")
        break
    elif old_time_choice == "end":
        g1_time = end_time
        g1_time_seconds = (datetime.strptime(g1_time, '%H:%M:%S.%f') - opening_time).total_seconds()
        print(f"You have chosen {g1_time} as your Chart 1 time.")
        print(f"{g1_time_seconds} seconds after 9 AM")
        break
    else:
        # If new time selected
        print("You have chosen to select a new time.")
        # Same loop as Task 1
        while True:
            g1_time = input("Please enter a time for Chart 1 in HH:MM:SS or HH:MM:SS.fff, where 'f' is a fraction of a second (to 3 DP). Trading starts at 09:00 and ends at 17:30.").strip()
            if g1_time == '':
                print("You have not entered a value.")
                # Break so that user can escape, if 'esc' pressed.
                break
            elif find_time(g1_time) == False:
                print(f"'{g1_time}' is not a valid time. Please use 'HH:MM:SS' (or HH:MM:SS.fff).")
            # See if it is within the specified times.
            else:
                if len(g1_time) == 8:
                    ms = '.000'
                    g1_time = g1_time + ms
                if datetime.strptime(g1_time, '%H:%M:%S.%f') > closing_time:
                    print(f"Error. {g1_time} is after 17:30:00. Please enter an earlier time.")
                elif datetime.strptime(g1_time, '%H:%M:%S.%f') < opening_time:
                    print(f"Error. {g1_time} is before 09:00:00. Please enter a later time.")
                else:
                    g1_time_seconds = (datetime.strptime(g1_time, '%H:%M:%S.%f') - opening_time).total_seconds()
                    print(f"You have chosen {g1_time} as your Chart 1 time.")
                    print(f"{g1_time_seconds} seconds after 9 AM")
                    break
        break
