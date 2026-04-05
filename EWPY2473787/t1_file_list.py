file_list = pd.DataFrame({'filename': dataset_list, 
                          'date': [find_date(file) for file in dataset_list], 
                          'lob_or_tapes': ['LOB' if 'LOB' in file else 'tapes' for file in dataset_list]})


file_list = file_list.sort_values(by = 'date')

file_list.reset_index(drop=True, inplace=True)

file_list.head()