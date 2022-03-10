import Hypothesis
import Data_Visualisation
import streamlit as st
import pandas as pd
import numpy as np
import scipy as stats
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊")
    

PAGES = {
    "Data Visualisation": Data_Visualisation,
    "Hypothesis Testing": Hypothesis
}

###### Multi Pages
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
