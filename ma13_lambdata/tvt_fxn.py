#ma13_lambdata/tvt_fxn.py

def tvt_split(df):
    """
    simple function to create a test/validate/train split on a dataset
    """
    from sklearn.model_selection import train_test_split

    #first declare train and test
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    #then decalre train and val
    train, val = train_test_split(train, test_size=0.2, random_state=42)
    
    return train, test, val