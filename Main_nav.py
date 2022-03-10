import Hypothesis
import Data_Visualisation
import streamlit as st

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
