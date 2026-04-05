# Notify user 
print(f"Output of {output_choice} {file_type_input} files:")

# Change to data set directory
os.chdir(data_set_directory)

# Call correct function as specified
if file_type_input == "tapes" and  output_choice == "verbatim":
    t1_user_output = vb_tape_files(selected_files, start_time_seconds, end_time_seconds, export_choice, output_dir)
if file_type_input == "tapes" and output_choice == "summary":
    t1_user_output = process_tape_files(selected_files, start_time_seconds, end_time_seconds, export_choice, output_dir)
if file_type_input == "lob" and output_choice == "verbatim":
    t1_user_output = vb_lob_files(selected_files, start_time_seconds, end_time_seconds, export_choice, output_dir)
if file_type_input == "lob" and output_choice == "summary":
    t1_user_output = process_lob_files(selected_files, start_time_seconds, end_time_seconds, export_choice, output_dir)
    
# Notify user
print("Output saved as object 't1_user_output'")
# Reset directory
os.chdir(zip_directory)