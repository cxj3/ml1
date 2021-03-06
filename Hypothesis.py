import streamlit as st
import pandas as pd
import numpy as np
import scipy as stats
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('Supermarket Sales - Hypothesis')

    ### import dataset
    df = pd.read_csv('supermarket_sales - Sheet1.csv')

    Product_Line_Gross_Income = df[['Product line','gross income']].groupby('Product line').mean()
    st.write(Product_Line_Gross_Income.sort_values(by='gross income', ascending=False,))

    st.write(
    "From the table above it's clear that the most successful (biggest average gross income) is coming from Home and lifestyle and the least successful (lowest average gross income) is coming from Sports and travel. Lets check how both categories compared."
    )


    # Query data of Gross income in Product line = Home and lifestyle
    Home_and_lifestyle = df[df['Product line'] == ('Home and lifestyle')]
    Home_and_lifestyle_gross_income = Home_and_lifestyle['gross income']
    Home_and_lifestyle_gross_income

    # Query data of usd_pledged_real in category = Tabletop Games
    Fashion_accessories= df[df['Product line'] == ('Fashion accessories')]
    Fashion_accessories_gross_income = Fashion_accessories['gross income']
    Fashion_accessories_gross_income

    
    st.subheader('Two Sample TTest - The Hypothesis is:')
    st.write(
    '- Null Hypothesis (H0):μHome and lifestyle = μSports and travel'
    '(Average gross income of Home and lifestyle is **not significantly different** from the average gross income of Sports and travel)'
    )
    
    st.write(
    '- Alternative Hypothesis (H1): μHome and lifestyle != μSports and travel'
    '(Average gross income of Home and lifestyle is **significantly different** from the average gross income of Sports and travel)'
    )

    # Finding P-value and t-statistics of the hypothesis
    t_stat, p_val = stats.ttest_ind(Home_and_lifestyle_gross_income,Fashion_accessories_gross_income)
    print('P-value:',p_val) #the p-value isn't divided by 2 since the output is two-sided p-value
    print('t-statistics:',t_stat)

    st.write(
    'When we run the two indipendent samples with a threshold of 0.05, we got this as the result:'
    'P-value: 0.5018922633919138'
    't-statistics: 0.672211969325253'
    )

    # Create samples of old and new page
    Home_and_lifestyle_pop = np.random.normal(Home_and_lifestyle_gross_income.mean(),Home_and_lifestyle_gross_income.std(),500)
    Fashion_accessories_pop = np.random.normal(Fashion_accessories_gross_income.mean(),Fashion_accessories_gross_income.std(),5000)

    # Ploting the graph below
    # confidence interval with critical value 0.05
    ci = stats.norm.interval(0.95, Home_and_lifestyle_gross_income.mean(), Home_and_lifestyle_gross_income.std())
    fig, ax = plt.subplots(figsize=(16,5))

    sns.distplot(Home_and_lifestyle_pop, label='Home and lifestyle',color='blue')
    sns.distplot(Fashion_accessories_pop, label='Fashion accessories',color='red')


    plt.axvline(Home_and_lifestyle_gross_income.mean(), color='blue', linewidth=2, label='Home and lifestyle Mean')
    plt.axvline(Fashion_accessories_gross_income.mean(), color='red',  linewidth=2, label='Fashion accessories Mean')

    plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
    plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2)

    plt.axvline(Home_and_lifestyle_pop.mean()+t_stat*Home_and_lifestyle_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
    plt.axvline(Home_and_lifestyle_pop.mean()-t_stat*Home_and_lifestyle_pop.std(), color='black', linestyle='dashed', linewidth=2)

    ax.legend()
    st.pyplot(fig)

    st.subheader('Conclusion')
    st.write(
    'Based on the hypothesis test, we can conclude that the H0 is accepted. The Average gross income of Home and lifestyle is **not significantly different** from the average gross income of Sports and travel.'
    )
