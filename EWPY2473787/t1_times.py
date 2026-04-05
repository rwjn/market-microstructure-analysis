opening_time = datetime.strptime('09:00:00.000', '%H:%M:%S.%f')
closing_time = datetime.strptime('17:30:00.000', '%H:%M:%S.%f')


while True:
    start_time = input("Please enter a start time in 24H format HH:MM:SS, or HH:MM:SS.fff, where 'f' is a fraction of a second (to 3 DP). Trading starts at 9:00 and ends at 17:30.").strip()
    if start_time == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    elif find_time(start_time) == False:
        print(f"'{start_time}' is not a valid time. Please use 'HH:MM:SS' (or HH:MM:SS.fff).")
    # See if it is within the specified times.
    else:
        if len(start_time) == 8:
            ms = '.000'
            start_time = start_time + ms
        if datetime.strptime(start_time, '%H:%M:%S.%f') > closing_time:
            print(f"Error. {start_time} is after 17:30:00. Please enter an earlier time.")
        elif datetime.strptime(start_time, '%H:%M:%S.%f') < opening_time:
            print(f"Error. {start_time} is before 09:00:00. Please enter a later time.")
        else:
            start_time_seconds = (datetime.strptime(start_time, '%H:%M:%S.%f') - opening_time).total_seconds()
            print(f"You have chosen {start_time} as your starting time.")
            print(f"{start_time_seconds} seconds after 9 AM")
            while True:
                end_time = input("Please enter an end time in 24H format HH:MM:SS, or HH:MM:SS.fff, where 'f' is a fraction of a second, to 3 DP. Trading starts at 9:00 and ends at 17:30").strip()
                if end_time == '':
                    print("You have not entered a value.")
                    # Break so that user can escape, if 'esc' pressed.
                    break
                elif find_time(end_time) == False:
                    print(f"'{end_time}' is not a valid time. Please use 'HH:MM:SS' (or HH:MM:SS.fff).")
                else:
                    if len(end_time) == 8:
                        ms = '.000'
                        end_time = end_time + ms
                    if datetime.strptime(end_time, '%H:%M:%S.%f') > closing_time:
                        print(f"Error. {end_time} is after 17:30:00. Please enter an earlier time.")
                    elif datetime.strptime(end_time, '%H:%M:%S.%f') < opening_time:
                        print(f"Error. {end_time} is before 09:00:00. Please enter a later time.")
                    # Check if time is before start time, if the user specifies a single day.
                    elif date_input == end_date_input and datetime.strptime(end_time, '%H:%M:%S.%f') < datetime.strptime(start_time, '%H:%M:%S.%f'):
                        print(f"Error. {end_time} is before start time ({start_time}). Please enter a later time.")
                    else:
                        end_time_seconds = (datetime.strptime(end_time, '%H:%M:%S.%f') - opening_time).total_seconds()
                        print(f"You have chosen {end_time} as your ending time.")
                        print(f'{end_time_seconds} seconds after 9 AM.')
                        break 
            break

