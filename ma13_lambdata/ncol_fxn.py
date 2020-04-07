#ma13_lambdata/ncol_fxn.py
#function to take a given list, turn it into a series and append it to a dataframe as a new column

def new_column(df, series, header):
    #first, make sure input is a df 
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Inputted object is not a DataFrame')

    #thenm, make sure the column isn't in df already
    if header in df.columns or not isinstance(header, str):
        raise KeyError('List is not a string or already in the DataFrame')

    #make copy of df to keep pandas happy
    df1 = df.copy()
    if isinstance(series, list):
        if (df.shape[0] == len(series)):
            series = pd.Series(series)
            df1[header] = series
        else:
            raise ValueError('The length of given list is not the same as the DataFrame')
    else:
        raise ValueError('Input is not a list')

    return df1

if __name__ == "__main__":
    pass