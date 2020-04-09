#ma13_lambdata/null_fxn.py

def col_nulls(df):
    """
    given a dataframe, returns which columns contain null values
    """
    import pandas as pd
    import numpy as np
    
    series = dataframe.isnull().any()
    null_columns = pd.DataFrame(series, columns=['Nulls'])
    null = False
    for i in range(len(null_columns)):
        if null_columns['Nulls'].iloc[i]:
            null = True
            return f'Column "{null_columns.index[i]}" in the dataframe contains null values'
    if not null:
        return f'This dataframe contains no null values'
