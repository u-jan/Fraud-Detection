

## Readme
You are a contract data scientist/consultant hired by a new e-commerce site to try to weed out fraudsters.
The company's expences increase if a customer buys tickets for a fraud event. Because by law
the refund is expected. Fraudsters win, the company loses not only money but also credibility.

### Data: df.columns

(['acct_type', 'approx_payout_date', 'body_length', 'channels', 'country',
       'currency', 'delivery_method', 'description', 'email_domain',
       'event_created', 'event_end', 'event_published', 'event_start',
       'fb_published', 'gts', 'has_analytics', 'has_header', 'has_logo',
       'listed', 'name', 'name_length', 'num_order', 'num_payouts',
       'object_id', 'org_desc', 'org_facebook', 'org_name', 'org_twitter',
       'payee_name', 'payout_type', 'previous_payouts', 'sale_duration',
       'sale_duration2', 'show_map', 'ticket_types', 'user_age',
       'user_created', 'user_type', 'venue_address', 'venue_country',
       'venue_latitude', 'venue_longitude', 'venue_name', 'venue_state'],
      dtype='object')


### Step_1: Explore
- Explored the data
- Generated target 

## Step_2: EDA
- Took notes about feature engineering
- Checked out corrolations
- Scatter plots to find out which predictors deliver signal
- Analis on target.
- Profit analisis

## Step_3: Modelling
- Engineered features
- NLP(parse - tokenization)
- Pipeline Model(@ src doc.)\
- ROC Curve
- Profit Curve