import pandas as pd
import numpy as np

def preprocess(df):
    # convert 'order_date' to datetime
    df['date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')
    # convert 'order_time' to time format
    df['time'] = pd.to_datetime(df['order_time'],format='%H:%M:%S').dt.time
    # Calculate the 'Amount' column
    df['Amount'] = df['quantity']*df['unit_price']
    df['hour'] = pd.to_datetime(df['order_time'], format='%H:%M:%S').dt.hour
    return df
