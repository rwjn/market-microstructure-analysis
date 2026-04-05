opening_time = datetime.strptime('09:00:00.000', '%H:%M:%S.%f')
closing_time = datetime.strptime('17:30:00.000', '%H:%M:%S.%f')

# Again, here we use a nested 'while' loop.

while True:
    old_time_choice = input("For Chart 2's start time, would you like to use your specified start or end times from Task 1? Enter 'start' for previous start time, 'end' for previous end time, or 'new' to specify a new time.").strip().lower()
    old_time_choice_list = ['start', 'end', 'new']
    if old_time_choice == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    elif old_time_choice not in old_time_choice_list:
        print(f"'{old_time_choice}' not recognised. Please enter 'start', 'end' or 'new'.")
    elif old_time_choice == "start":
        g2_start_time = start_time
        g2_start_time_seconds = (datetime.strptime(g2_start_time, '%H:%M:%S.%f') - opening_time).total_seconds()
        print(f"You have chosen {g2_start_time} as your Chart 2 start time.")
        print(f"{g2_start_time_seconds} seconds after 9 AM")
        break
    elif old_time_choice == "end":
        g2_start_time = end_time
        g2_start_time_seconds = (datetime.strptime(g2_start_time, '%H:%M:%S.%f') - opening_time).total_seconds()
        print(f"You have chosen {g2_start_time} as your Chart 2 start time.")
        print(f"{g2_start_time_seconds} seconds after 9 AM")
        break
    else:
        print("You have chosen to select a new time.")
        while True:
            g2_start_time = input("Please enter a start time for Chart 2 in HH:MM:SS or HH:MM:SS.fff, where 'f' is a fraction of a second (to 3 DP). Trading starts at 09:00 and ends at 17:30.").strip()
            if g2_start_time == '':
                print("You have not entered a value.")
                # Break so that user can escape, if 'esc' pressed.
                break
            elif find_time(g2_start_time) == False:
                print(f"'{g2_start_time}' is not a valid time. Please use 'HH:MM:SS' (or HH:MM:SS.fff).")
            # See if it is within the specified times.
            else:
                if len(g2_start_time) == 8:
                    ms = '.000'
                    g2_start_time = g2_start_time + ms
                if datetime.strptime(g2_start_time, '%H:%M:%S.%f') > closing_time:
                    print(f"Error. {g2_start_time} is after 17:30:00. Please enter an earlier time.")
                elif datetime.strptime(g2_start_time, '%H:%M:%S.%f') < opening_time:
                    print(f"Error. {g2_start_time} is before 09:00:00. Please enter a later time.")
                else:
                    g2_start_time_seconds = (datetime.strptime(g2_start_time, '%H:%M:%S.%f') - opening_time).total_seconds()
                    print(f"You have chosen {g2_start_time} as your Chart 2 start time.")
                    print(f"{g2_start_time_seconds} seconds after 9 AM")
                    break
        break

while True:
    old_time_choice = input("For Chart 2's end time, would you like to use your specified start or end times from Task 1? Enter 'start' for previous start time, 'end' for previous end time, or 'new' to specify a new time.").strip().lower()
    old_time_choice_list = ['start', 'end', 'new']
    if old_time_choice == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    elif old_time_choice not in old_time_choice_list:
        print(f"'{old_time_choice}' not recognised. Please enter 'start', 'end' or 'new'.")
    elif old_time_choice == "start":
        g2_end_time = start_time
        g2_end_time_seconds = (datetime.strptime(g2_end_time, '%H:%M:%S.%f') - opening_time).total_seconds()
        if g2_date_input == g2_end_date_input and datetime.strptime(g2_end_time, '%H:%M:%S.%f') <= datetime.strptime(g2_start_time, '%H:%M:%S.%f'):
            print(f"Error. {g2_end_time} must be later than start time ({g2_start_time}). Please enter a later time.")
        else: 
            print(f"You have chosen {g2_end_time} as your Chart 2 end time.")
            print(f"{g2_end_time_seconds} seconds after 9 AM")
            break
    elif old_time_choice == "end":
        g2_end_time = end_time
        g2_end_time_seconds = (datetime.strptime(g2_end_time, '%H:%M:%S.%f') - opening_time).total_seconds()
        if g2_date_input == g2_end_date_input and datetime.strptime(g2_end_time, '%H:%M:%S.%f') <= datetime.strptime(g2_start_time, '%H:%M:%S.%f'):
            print(f"Error. {g2_end_time} must be later than start time ({g2_start_time}). Please enter a later time.")
        else: 
            print(f"You have chosen {g2_end_time} as your Chart 2 end time.")
            print(f"{g2_end_time_seconds} seconds after 9 AM")
            break
    else:
        print("You have chosen to select a new time.")
        while True:
            g2_end_time = input("Please enter a time for Chart 1 in HH:MM:SS or HH:MM:SS.fff, where 'f' is a fraction of a second (to 3 DP). Trading starts at 09:00 and ends at 17:30.").strip()
            if g2_end_time == '':
                print("You have not entered a value.")
                # Break so that user can escape, if 'esc' pressed.
                break
            elif find_time(g2_end_time) == False:
                print(f"'{g2_end_time}' is not a valid time. Please use 'HH:MM:SS' (or HH:MM:SS.fff).")
            # See if it is within the specified times.
            else:
                if len(g2_end_time) == 8:
                    ms = '.000'
                    g2_end_time = g2_end_time + ms
                if datetime.strptime(g2_end_time, '%H:%M:%S.%f') > closing_time:
                    print(f"Error. {g2_end_time} is after 17:30:00. Please enter an earlier time.")
                elif datetime.strptime(g2_end_time, '%H:%M:%S.%f') < opening_time:
                    print(f"Error. {g2_end_time} is before 09:00:00. Please enter a later time.")
                elif g2_date_input == g2_end_date_input and datetime.strptime(g2_end_time, '%H:%M:%S.%f') <= datetime.strptime(g2_start_time, '%H:%M:%S.%f'):
                    print(f"Error. {g2_end_time} must be later than start time ({g2_start_time}). Please enter a later time.")
                else:
                    g2_end_time_seconds = (datetime.strptime(g2_end_time, '%H:%M:%S.%f') - opening_time).total_seconds()
                    print(f"You have chosen {g2_end_time} as your Chart 2 end time.")
                    print(f"{g2_end_time_seconds} seconds after 9 AM")
                    break
        break

# Warning for time length, to try to mitigate a crash.
if g2_date_input == g2_end_date_input:
    time_range = g2_end_time_seconds - g2_start_time_seconds
    if time_range > 200:
        print(f"Warning time range ({time_range} seconds) is longer than recommended. Please consider re-selecting start/end time.")

