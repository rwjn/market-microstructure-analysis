while True:
    # First we need to specify if the user is interested in LOB or tapes files
    file_type_choices = ['lob', 'tapes']
    file_type_input = input("Please enter 'lob' for LOB data or 'tapes' for tape data").lower().strip()
    if file_type_input == '':
        print("You have not entered a value.")
        # Break so that user can escape, if 'esc' pressed.
        break
    if file_type_input not in file_type_choices:
        print(f"'{file_type_input}' is not recognised. Please enter either 'lob' or 'tapes'")
    else:
        print(f"You have chosen {file_type_input} data.")
        break