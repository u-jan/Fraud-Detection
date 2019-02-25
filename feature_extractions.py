import pandas as pd
import numpy as np

def make_target(df):
    output = ['fraud' in val for val in df['acct_type']]
    return output

def dummy(df, col):
    ''' Function does not update df inplace 
    input:
    df (dataframe)
    col (string)
    '''
    dummies = pd.get_dummies(df[col], prefix=col)
    return df.drop(col, axis=1).merge(dummies, left_index=True, right_index=True)


def extract_features(df, col_wanted, col_dummies_needed):
    #df = pd.read_json(path)
    output_df = df[col_wanted]
    for col in col_dummies_needed:
        output_df = dummy(output_df, col)
    return output_df

        
def extract_ticket_tiers(df):
    '''
    output df will drop ticket_types col
    '''
    ticket_types_length = []
    for ticket_type in df['ticket_types'].values:
        ticket_types_length.append(len(ticket_type))
    output_df = df.drop('ticket_types', axis=1)
    output_df['ticket_type_length'] = ticket_types_length
    return output_df


def extract_venue_address_given(df):
    mask = df['venue_address'] == ''
    df['no_address'] = mask
    df['no_address'] =  df['no_address'].map({True:0, False:1})
    X = df.drop('venue_address', axis=1)
    return X






''' How to run it

col_wanted = ['description', 'user_age', 'country', 
                  'ticket_types', 'venue_address', 'channels', 
                  'has_logo', 'delivery_method']
col_dummies_needed = ['delivery_method', 'country']

df_test = extract_features('data/data.json', col_wanted, col_dummies_needed)
df_test = extract_ticket_tiers(df_test)
df_test = extract_venue_address_given(df_test)
df_test.head()

'''