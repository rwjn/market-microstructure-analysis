import re
from datetime import datetime

def find_date(file):
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', file) 
    try:
        date = date_match.group(0)
        datetime.strptime(date, '%Y-%m-%d')
        return date
    except (ValueError, AttributeError):
        return False