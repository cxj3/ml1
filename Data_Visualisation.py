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
    st.subheader('By: Charissa Janto - Batch 09')
    st.markdown('Data Visualisation')


    ############### Import Data
    df = pd.read_csv('/Users/charissa.janto/Desktop/Hactiv8/GitHub/Milestone/ml1/supermarket_sales - Sheet1.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%d-%m-%y')

    if  st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)
        st.write('This Dataset has 1000 rows and 17 columns, which consist of Invoice ID, Branch, City, Customer type, Gender, Product line, Unit price, Quantity, Tax 5%, Total, DateTime, Payment, cogs, gross margin percentage, gross income, Rating')


    ############ Column and rows
    baris1_col1,baris1_col2,baris1_col3 = st.columns((2,2,1))


    ############ Purchase in Cities
    st.subheader('Exploration of purchases Cities / Branch')

    col1, col2 = st.columns(2)
    with col1:
        st.write('**Number of purchase in a particular city**')
        city_value= df['city'].value_counts()
        st.bar_chart(city_value)

    st.write('By looking at the data, we know that:')
    st.write('- Yangon is branch A')
    st.write('- Mandalay is branch B')
    st.write('- Naypyitaw is branch C.')
    st.write('From the exploration above we know that **Yangon is the most active city / branch** (340 purchases), but **Naypyitaw makes the most Gross income** ($5265.17)')
    
    with col2:
        # Find Sum Gross Income from different Cities
        City_Gross_Income = df[['city','gross income']].groupby('city').sum()
        City_Gross_Income.sort_values(by='gross income', ascending=False,)
   

        # Plot Sum Gross Income from different Cities
        st.write('**Gross income made in a particular city**')
        fig, ax = plt.subplots(figsize=(10, 10))
        City_Gross_Income.plot(kind='bar',color='steelblue',ax=ax)
        ax.set_xlabel('Sum of Gross Income')
        ax.set_title('Gross income in different cities')
        st.pyplot(fig)


    ############ Purchase of Product lines
    st.subheader('Exploration of product line purchases')

    #######Plot 1 - Number of purchase in product lines
    fig = go.Figure(
    go.Pie(
    labels = df['product line'].unique(),
    values = df['product line'].value_counts(),
    hoverinfo = "label+percent",
    textinfo = "value"
    ))
    st.write('**Number of purchases in product lines**')
    st.plotly_chart(fig)

    st.write('**Gross income created by product lines**')
    
    #Find the sum of gross profit from each product line
    Product_Line_Gross_Income = df[['product line','gross income']].groupby('product line').sum()
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

    start_color, end_color = st.select_slider(
     'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('red', 'blue'))
    st.write('You selected wavelengths between', start_color, 'and', end_color)
