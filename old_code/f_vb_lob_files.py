import pandas as pd   

import regex as re

import os

def vb_lob_files(file_list, start_time_seconds, end_time_seconds, export_choice = "no", output_dir = "",time_col = 1):
    # Dictionary to store processed dataframes
    processed_dfs = {}

    for fname in file_list:
        extension = fname[-4:]
        if extension == '.csv':
            # Read file data
            df = pd.read_csv(fname, header = None)
            # If file name is the same as start date:
            if fname == file_list[0]:
                # Then only take rows after the start time.
                df = df[df[time_col] >= start_time_seconds]
            # If file name is the same as the end date:
            if fname == file_list[-1]:
                # Then only take rows before the end.
                df = df[df[time_col] <= end_time_seconds]

            # Add processed df to dictionary 
            processed_dfs[fname] = df

            # Export to CSV if export_choice is 'yes'
            if export_choice.lower() == "yes":
                # Add string to start of fname to differentiate it from input files.
                output_fname = 'VB_Output_' + fname
                output_filename = os.path.join(output_dir, output_fname)
                df.to_csv(output_filename, index=False, header = None)
                print(f'Exported {fname} as {output_filename}')
        else:
            print(f'FAIL: file with extension={extension} can\'t be handled')

    return processed_dfs

# ## Testing
# file_list = ['UoB_Set01_2024-01-02LOBs.csv', 'UoB_Set01_2024-01-03LOBs.csv'] 
# start_time_seconds = 0
# end_time_seconds = 5
# result_dfs = vb_lob_files(file_list, start_time_seconds, end_time_seconds, "no")
# times = list(result_dfs.keys())
# print(times)
