from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FF6347;
    }
</style>
""", unsafe_allow_html=True)
def show():
    with st.sidebar:
        selected = option_menu(
            menu_title = None,
            options = ["Text", "Image"], #required
            default_index = 0, 
        )
        return selected


