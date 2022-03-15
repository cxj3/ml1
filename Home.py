import streamlit as st
import pandas as pd

def app():
    st.title('Supermarket Sales Analysis')
    st.write('By: Charissa Janto - Batch 09')

############### Import Data
    df = pd.read_csv('/Users/charissa.janto/Desktop/Hactiv8/GitHub/Phase 0/Milestone/ml1/supermarket_sales - Sheet1.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)

    st.write('The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.')

    with st.expander("See Dataset"):
        st.subheader('Sales Data')
        st.write(df)
        st.write(
            """
            ##### This Dataset has 1000 rows and 17 columns, which consist of:
            - Branch: Branch of supercenter (3 branches are available identified by A, B and C).
            - City: Location of supercenters
            - Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
            - Gender: Gender type of customer
            - Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
            - Unit price: Price of each product in $
            - Quantity: Number of products purchased by customer
            - Tax: 5% tax fee for customer buying
            - Total: Total price including tax
            - Date: Date of purchase (Record available from January 2019 to March 2019)
            - Time: Purchase time (10am to 9pm)
            - Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
            - COGS: Cost of goods sold
            - Gross margin percentage: Gross margin percentage
            - Gross income: Gross income
            - Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)""")