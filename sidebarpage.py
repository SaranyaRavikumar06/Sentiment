from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu
def show():
    with st.sidebar:
        st.markdown("""
        <style>
            .sidebar a.selected {
                background-color: #ff0000;
                color: #00ffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
        )
        selected = option_menu(
            menu_title = None,
            options = ["Text", "Image"], #required
            default_index = 0, 
        )
        return selected


