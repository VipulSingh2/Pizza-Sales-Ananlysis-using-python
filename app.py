import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
#import mplcyberpunk  # Uncomment if cyberpunk style is needed
import visual

# Setting the page config
st.set_page_config(page_title="🍕 Pizza Sales Analysis", layout="wide")

# Title
st.title("🍕 Pizza Sales Analysis 🍕")

# Load the dataset
df = pd.read_csv(r'pizzas.csv')

# Preprocess the data
preprocessed_df = visual.preprocess(df)

# Display the preprocessed dataframe
st.dataframe(preprocessed_df)

# Calculate KPIs and analysis metrics
total_sales, total_orders, total_sold, most_orded, wrost_orded, daily, category, size, pizza_sold, line = visual.kpi_plotter(df)

# Display KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", value=round(total_sales, 2))
with col2:
    st.metric("Total Orders", value=total_orders)
with col3:
    st.metric("Total Pizzas Sold", value=round(total_sold, 2))

# Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("10 Most Ordered Pizzas")
    fig, ax = plt.subplots()
    ax.bar(x=most_orded.index, height=most_orded.values, width=0.6, color='lime')
    plt.xlabel("Pizza Name", fontsize=15)
    plt.ylabel("Count", fontsize=15)
    plt.xticks(rotation=90, fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(fig)

with col2:
    st.subheader("10 Least Ordered Pizzas")
    fig, ax = plt.subplots()
    ax.bar(x=wrost_orded.index, height=wrost_orded.values, width=0.6, color='greenyellow')
    plt.xlabel("Pizza Name", fontsize=15)
    plt.ylabel("Count", fontsize=15)
    plt.xticks(rotation=90, fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pizza Category Distribution")
    fig, ax = plt.subplots()
    ax.pie(category, labels=category.index, autopct="%0.1f%%")
    plt.legend(loc='upper left')
    st.pyplot(fig)

with col2:
    st.subheader("% Sales by Pizza Size")
    fig, ax = plt.subplots()
    explode = [0.1 if i == size.idxmax() else 0 for i in range(len(size))]
    ax.pie(size, labels=size.index, explode=explode, autopct="%0.1f%%")
    plt.legend(loc='upper left')
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pizzas Sold by Category")
    fig, ax = plt.subplots()
    ax.bar(x=category.index, height=category.values, width=0.4, color='aqua')
    plt.xlabel("Category", fontsize=15)
    plt.ylabel("Pizzas Sold", fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(fig)

with col2:
    st.subheader("Daily Order Trend")
    fig, ax = plt.subplots()
    ax.bar(x=daily.index, height=daily.values, width=0.6, color='fuchsia')
    plt.xlabel("Days", fontsize=15)
    plt.ylabel("Orders", fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pizzas Sold by Category")
    fig, ax = plt.subplots()
    ax.bar(x=category.index, height=category.values, width=0.4, color='greenyellow')
    plt.xlabel("Category", fontsize=15)
    plt.ylabel("Pizzas Sold", fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    st.pyplot(fig)

with col2:
    st.subheader("Daily Sales Trend")
    fig, ax = plt.subplots()
    ax.plot(line.index, line.values, marker='o')
    plt.xlabel("Date", fontsize=15)
    plt.ylabel("Sales", fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(fig)
