import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import mplcyberpunk
import visual

# setting the page config
st.set_page_config("🍕 Sales Analysis")
# Load the dataset
st.title("🍕Pizza Sales Analysis🍕")
df = pd.read_csv(r'pizzas.csv')
