import numpy as np
import pandas as pd
from sqlalchemy import create_engine

events_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='allevents')
users_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='allusers')
category_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='category')
date_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='date2008')
listings_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='listings')
sales_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='sales')
venue_df = pd.read_excel('CA1_Ecommerce_database (1).xlsx', sheet_name='venue')


events_df.to_sql('event_sql', con=engine, schema='samuel', index=False, if_exists="replace")
users_df.to_sql('users_sql', con=engine, schema='samuel', index=False, if_exists="replace")
category_df.to_sql('category_sql', con=engine, schema='samuel', index=False, if_exists="replace")
date_df.to_sql('date_sql', con=engine, schema='samuel', index=False, if_exists="replace")
listings_df.to_sql('listings_sql', con=engine, schema='samuel', index=False, if_exists="replace")
sales_df.to_sql('sales_sql', con=engine, schema='samuel', index=False, if_exists="replace")
venue_df.to_sql('event_sql', con=engine, schema='samuel', index=False, if_exists="replace")
