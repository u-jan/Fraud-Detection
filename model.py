import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline

from feature_extractions import make_target, extract_features, extract_ticket_tiers, extract_venue_address_given, dummy





#features selection
features = ['user_age', 'country', 
                  'ticket_types', 'venue_address', 'channels', 
                  'has_logo', 'delivery_method']


#data loading, create X, y
df = pd.read_json('data/data.json')
df_test = extract_features(df, features, ['delivery_method', 'country'])
df_test = extract_ticket_tiers(df_test)
X = extract_venue_address_given(df_test)
y = make_target(df)


#make model
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2)
log = LR()
pipeline = Pipeline([('log', log)])
pipeline.fit(X_train, y_train)



filename = 'log_reg.pkl'
pickle.dump(pipeline, open(filename, 'wb'))