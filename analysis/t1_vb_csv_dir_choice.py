# First choice, summary or verbatim data. 
# While loop until correctly specified.
while True:
    output_choice = input("Please choose if you prefer 'summary' or 'verbatim' data:").lower().strip()
    output_choice_list = ['summary', 'verbatim']
    # Escape option
    if output_choice == '':
        print("You have not entered a value.")
        break
    elif output_choice not in output_choice_list:
        print(f"{output_choice} is not recognised. Please input either 'summary' or 'verbatim'")
    else:
        print(f"You have selected '{output_choice}'")
        break

# CSV export choice.
while True:
    export_choice = input("Would you like to export the output to a CSV file (please input 'yes' or 'no')").lower().strip()
    export_choice_list = ['yes', 'no']
    # Escape option
    if export_choice == '':
        print("You have not entered a value.")
        break
    elif export_choice not in export_choice_list:
        print(f"{export_choice} is not recognised. Please input either 'yes' or 'no'.")
    else:
        print(f"You have selected '{export_choice}' to exporting as a CSV.")
        break

# If user chooses, to export, they can specify directory.
if export_choice == "yes":
    while True:
        output_dir = input("Please select an output directory.")
        if output_dir == '':
            print("You have not entered a value for output directory.")
            break
        elif not os.path.isdir(output_dir):
                # Make directory if it doesn't exist
                os.makedirs(output_dir)  
                # Notify user
                print(f"Directory {output_dir} created.")
                break
        else: 
            print(f"You have selected {output_dir} as your output directory.")
            break
# If the user does not want to export, we still need a value, so the functions can be called.
else:
    output_dir = ""