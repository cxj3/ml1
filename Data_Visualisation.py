import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import scipy as stats
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def app():
    st.title('Sales - Analysis and Visualization')

    ############### Import Data
    df = pd.read_csv('supermarket_sales - Sheet1.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    df['date']=  pd.to_datetime(df['date'], format = '%m/%d/%Y').dt.date

    with st.expander("Exploration on Cities / Branch"):
        st.subheader('Exploration of Cities / Branch Sales')
        st.write('Researching different cities, will give a deepper insights on which city is more active interms of sales, and also which city creates the most gross income. From looking at the data set, we know that:')
        st.write("""
        - Yangon is branch A
        - Mandalay is branch B
        - Naypyitaw is branch C""")

        st.write('The date in the data set has a range between', df['date'].min(), 'and', df['date'].max())

        ########Slider
        date_options = df['date'].unique()
        Date = st.slider(
            label= 'Slide and pick which range of dates to explore',
            min_value= df['date'].min(),
            max_value= df['date'].max(),
            value= (df['date'].min(),
            df['date'].max()))

        df_select_date = df[(df["date"] >= Date[0]) & 
                                (df["date"] <= Date[1]) ]

        ############ Column and rows
        baris1_col1,baris1_col2,baris1_col3 = st.columns((2,2,1))


        ############ Purchase in Cities
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Number of purchase in a particular city**')
            city_value= df_select_date['city'].value_counts()
            st.bar_chart(city_value)


        ########## Sum Gross Income from different Cities
        with col2:
        
            City_Gross_Income = df_select_date[['city','gross income']].groupby('city').sum()
            City_Gross_Income.sort_values(by='gross income', ascending=False)
    

            # Plot Sum Gross Income from different Cities
            st.write('**Gross income made in a particular city**')
            fig, ax = plt.subplots(figsize=(10, 10))
            City_Gross_Income.plot(kind='bar',color='steelblue',ax=ax)
            ax.set_xlabel('Sum of Gross Income')
            ax.set_title('Gross income in different cities')
            st.pyplot(fig)
        
        # Description of findings 
        st.write('At 2019-01-01 until 2019-03-30, **Yangon is the most active city** / branch with 340 purchases, but **Naypyitaw makes the most Gross income** of $5265.17')


    with st.expander("Exploration of Product Lines"):
        st.subheader('Exploration of Sales in each Product Line')
        st.write('Doing more research on product line give an understanding on which products are more profitable for the supermarket and where are these products getting sold.')

        ###### Multi selector
        city_options = df['city'].unique()
        city = st.selectbox(
            label= 'Pick a city to explore',
            options= city_options
            )
        df_select_city= df[(df["city"] == city)]


        #######Plot 1 - Number of purchase in product lines    
        fig = go.Figure(
        go.Pie(
        labels = df_select_city['product line'].unique(),
        values = df_select_city['product line'].value_counts(),
        hoverinfo = "label+percent",
        textinfo = "value"
        ))
        st.write('**Number of purchases in product lines**')
        st.plotly_chart(fig)

        st.write('**Gross income created by product lines**')
        
        #Find the sum of gross profit from each product line
        Product_Line_Gross_Income = df_select_city[['product line','gross income']].groupby('product line').sum()
        Product_Line_Gross_Income.sort_values(by='gross income', ascending=False,)
        
        ####### Plot2 - Sum Gross Income from each product line
        fig, ax = plt.subplots(figsize=(10, 10))
        Product_Line_Gross_Income.plot(kind='barh',color='steelblue',ax=ax)
        ax.set_xlabel('Sum of Gross Income')
        ax.set_title('Gross income from product lines')
        st.pyplot(fig)


        st.write('By looking at the product line purchases data, we know that:')
        st.write('The number of purchases is quiet the same among all the product lines, with **most purchased product line: Health and beauty** - 178 purchses')
        st.write("There's no significalt difference between the total gross income in from each product lines. Eventhought the most purchased productline is Health and beauty, the **most gross income is made by: Food and beverages** - $2673.56 ")
