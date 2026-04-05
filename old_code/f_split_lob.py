# Split 'lob' column into two. 

def split_lob(lob):
    try:
        # The ']],' separates the bid and ask in the lob column.
        bid, ask = lob.split(']],')
    # Avoid crashing
    except ValueError:
        return lob, lob
    # Will return as 2 separate DF columns
    return bid, ask