
# This file uses Dave Cliffs 'OHLC.py' file, but as a function.
# In the .ipynb, user will specify chosen files with inputs 'file_list'.
# The user will also specify start and end times

import pandas as pd
import os

def vb_tape_files(file_list, start_time_seconds, end_time_seconds, export_choice="no", output_dir = "", time_col=2,):
    # Dictionary to store processed dataframes
    processed_dfs = {}
    
    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Read and process the dataframe
            df = pd.read_csv(fname, header = None)
            if fname == file_list[0]:
                df = df[df[time_col] >= start_time_seconds]
            if fname == file_list[-1]:
                df = df[df[time_col] <= end_time_seconds]
            
            # Store the processed dataframe
            processed_dfs[fname] = df
            
            # Export to CSV if export_choice is 'yes'
            if export_choice.lower() == "yes":
                # Add string to start of fname to differentiate it from input files.
                output_fname = 'VB_Output_' + fname
                output_filename = os.path.join(output_dir, output_fname)
                df.to_csv(output_filename, index=False, header = None)
                print(f'Exported {fname} as {output_filename}')
        else:
            print(f'FAIL: File with extension={extension} can\'t be handled')

    return processed_dfs

# # Testing:
# os.chdir("path/to/data")  # Set your working directory here
# file_list = ['UoB_Set01_2024-04-02tapes.csv']
# start_time_seconds = 10800.0
# end_time_seconds = 10805.0
# export_choice = "no"  # Set this based on your requirement outside the function
# result_dfs = vb_tape_files(file_list, start_time_seconds, end_time_seconds, export_choice=export_choice)

# # Accessing a specific processed dataframe
# print(result_dfs['UoB_Set01_2024-04-02tapes.csv'])
