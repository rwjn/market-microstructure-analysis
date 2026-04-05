import regex as re
from datetime import datetime

def find_time(input_time):
    try:
        if len(input_time) == 8:
            time_match = re.search(r'\d{2}:\d{2}:\d{2}', input_time) 
            ms = '.000'
            time = time_match.group(0)
            time = time + ms
            datetime.strptime(time, '%H:%M:%S.%f')
        else:
            time_match = re.search(r'\d{2}:\d{2}:\d{2}.\d{3}', input_time) 
            time = time_match.group(0)
            datetime.strptime(time, '%H:%M:%S.%f')
        return time
    except (ValueError, AttributeError):
        return False
    
find_time('09:00:00.000')