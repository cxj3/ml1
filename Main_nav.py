import Hypothesis
import Data_Visualisation
import Home
import streamlit as st


st.set_page_config(
    page_title="Supermarket Analysis",
    page_icon="🍔")
    

PAGES = {
    "Home": Home,
    "Data Visualisation": Data_Visualisation,
    "Hypothesis Testing": Hypothesis
}

###### Multi Pages
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
