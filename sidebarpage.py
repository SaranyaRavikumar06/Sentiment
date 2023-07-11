from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu

def show():
    with st.sidebar:
        selected = option_menu(
            menu_title = None,
            options = ["Text", "Image"], #required
            default_index = 0, 
        )
        return selected
def add_bg_from_url():
  st.markdown(
    """
 <style>
 .sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: yellow;
 }
 </style>
 """,
    unsafe_allow_html=True,
 )
add_bg_from_url() 

