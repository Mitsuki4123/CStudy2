import pandas as pd
import time
import numpy as np
import datetime
from icecream import ic

# encoding the timestamp data cyclically. See Medium Article.
def process_data(source):

    df = pd.read_csv(source)
        
    for ts in  df["count"]:
        df['sin_hour'] = np.sin(2*np.pi*ts)
        df['cos_hour'] = np.cos(2*np.pi*ts)
        # df['sin_day'] = np.sin(2*np.pi*ts)
        # df['cos_day'] = np.cos(2*np.pi*ts)
        # df['sin_month'] = np.sin(2*np.pi*ts)
        # df['cos_month'] = np.cos(2*np.pi*ts)

    return df

train_dataset = process_data('Data/success1.csv')
test_dataset = process_data('Data/success2.csv')

train_dataset.to_csv(r'Data/train_dataset.csv', index=False)
test_dataset.to_csv(r'Data/test_dataset.csv', index=False)
