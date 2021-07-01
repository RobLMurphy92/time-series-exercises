import pandas as pd
import requests

import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

def prepare_store_items_sale(df):
    #for this dataset dropping repetitive columns
    df.drop(columns = ['store', 'item'], inplace = True)
    #changin sale_amount to int.
    df.sale_amount = df.sale_amount.astype('int')
    # converting sale date to datetime
    df.sale_date = pd.to_datetime(df.sale_date)
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = (df.sale_amount * df.item_price)
    
    return df


def prepare_german(df):
    df.Date= pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df.fillna(0, inplace = True)
    return df
