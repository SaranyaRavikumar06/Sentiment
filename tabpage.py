from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu
def show():
    st.code("import extra_streamlit_components as stx")
    selected = st.tabs(["Text","Image"])
return selected
