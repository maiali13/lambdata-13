#ma13_lambdata/my_script.py

#GIVEN: dataframe with column called "abbrev" which has state abreviations
#GOAL: create a new column called "state_name" which has corresponing state name
import pandas

def state_convert(my_df):
    """
    function to convert state abbreviations to their full name
    """
    df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "FL", "TX"]})
    #print(df.head())

    names_map = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    df["state_name"] = df["abbrev"].map(names_map)
    return df

if __name__ == "__main__":
        
    df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "FL", "TX"]})
    full_df = state_convert(df)
    print(full_df.head())


    df2 = pandas.DataFrame({"abbrev": ["AL", "NY", "CA", "FL", "WA"]})
    full_df2 = state_convert(df2)
    print(full_df2.head())
