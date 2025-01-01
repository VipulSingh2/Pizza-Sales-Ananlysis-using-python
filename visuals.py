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
def kpi_plotter(df):
    # total Sales
    total_sales = df['Amount'].sum()
    # total orders
    total_orders = df.shape[0]
    # total pizzas sold
    total_sold = df['Total Orders'].sum()
    # most Orded pizzas
    most_orded = df['pizza_name'].value_counts().head(10)
    # less orded pizzas
    wrost_orded = df['pizza_name'].value_counts().tail(10)
    # daily trend plotting
    daily = df['Day'].value_counts()
    # category wiese plotting
    category = round((df['pizza_category'].value_counts()/df.shape[0])*100,2)
    # size wise plotting
    size = round((df['pizza_size'].value_counts()/df.shape[0])*100,2)
    # most sold pizzas
    pizza_sold = df.pizza_category.value_counts()
    # hourly trend
    line =  df['hour'].value_counts().sort_index()
    return total_sales,total_orders,total_sold,most_orded,wrost_orded,daily,category,size,pizza_sold,line
