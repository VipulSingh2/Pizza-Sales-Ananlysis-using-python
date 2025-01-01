import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
#import mplcyberpunk
import visual

# setting the page config
st.set_page_config("🍕 Sales Analysis")
# Load the dataset
st.title("🍕Pizza Sales Analysis🍕")
df = pd.read_csv(r'pizzas.csv')

# sending the data for the preprocessing
preprocessed_df = visual.preprocess(df)
# presenting the dataframe to the user
st.dataframe(preprocessed_df)
# making a button to show analysis

with st.form(key='plotting'):
    button = st.form_submit_button("Show Ananlysis")
    if button:
        total_sales,total_orders,total_sold,most_orded,wrost_orded,daily,category,size,pizza_sold,line = visual.kpi_plotter(df)
        col1,col2,col3 = st.columns(3)
        with col1:
            # making the metric or the KPI of the toal Sales
            st.metric("Toatl Sales",value = round(total_sales,2))
        with col2:
            st.metric("Total Orders",value = total_orders)
        with col3:
            st.metric("Total pizzas Sold",value = round(total_sold,2))
        col1,col2=st.columns(2)
        with col1:
            st.subheader("10 Most Orded Pizzas")
            plt.style.use('cyberpunk')
            fig,ax = plt.subplots()
            ax.bar(x = most_orded.index,height = most_orded.values,width = 0.6,color='lime')
            plt.xlabel("pizza Name",fontsize = 15)
            plt.ylabel("count",fontsize =15)
            plt.xticks(rotation = 90,fontsize = 15)
            plt.yticks(fontsize =15)
            st.pyplot(fig)
        with col2:
            st.subheader("10 wrost Orded Pizzas")
            plt.style.use('cyberpunk')
            fig,ax = plt.subplots()
            ax.bar(x = wrost_orded.index,height = wrost_orded.values,width = 0.6,color ='greenyellow')
            plt.xlabel("pizza Name",fontsize=15)
            plt.ylabel("count",fontsize =15)
            plt.xticks(rotation = 90,fontsize=15)
            plt.yticks(fontsize =15)
            st.pyplot(fig)
        col1,col2 =st.columns(2)
        with col1:
            st.subheader("Pizzas Category Distri")
            fig, ax = plt.subplots()
            ax.pie(category,labels = category.index,autopct = "%0.1f%%")
            plt.legend( loc='upper left')
            st.pyplot(fig)
        with col2:
            st.subheader("% Sales pizza Category")
            fig, ax = plt.subplots()
            ex = [0, 0, 0, 0, 0.3]
            ax.pie(size, labels=size.index, explode = ex,autopct="%0.1f%%")
            plt.legend(loc='upper left')
            st.pyplot(fig)
            
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("pizzas Sold category wise")
            fig,ax = plt.subplots()
            ax.bar(x = category.index,height = category.values,width = 0.4,color ='aqua')
            plt.xlabel("Days",fontsize=15)
            plt.ylabel("Orders",fontsize =15)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            st.pyplot(fig)
        with col2:
            st.subheader("Daily Order Trend")
            fig,ax = plt.subplots()
            ax.bar(x = daily.index,height = daily.values,width = 0.6,color ='fuchsia')
            plt.xlabel("Days",fontsize = 15)
            plt.ylabel("Orders",fontsize =15)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            st.pyplot(fig)
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("pizzas Sold by category")
            fig,ax = plt.subplots()
            ax.bar(x = category.index,height = category.values,width = 0.4,color ='greenyellow')
            plt.xlabel("Days",fontsize=15)
            plt.ylabel("Orders",fontsize=15)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            plt.grid()
            st.pyplot(fig) 
        with col2:
            st.subheader("Daily Sales Trend")
            fig,ax = plt.subplots()
            ax.plot(line.index,line.values,marker='o')
            plt.xlabel("Hours",fontsize=15)
            plt.ylabel("Orders",fontsize=15)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            st.pyplot(fig) 
                    
            
