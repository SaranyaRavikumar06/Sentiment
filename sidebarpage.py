from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu
def show():
    with st.sidebar:
        st.markdown( f"""
         <style>
         .stApp {{
             #background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background: content-box radial-gradient(#FF0000, white);
             #background-color:aquamarine;
             background-attachment: fixed;
             background-size: contain;
         }}
         </style>
         """,
         unsafe_allow_html=True)
        selected = option_menu(
            menu_title = None,
            options = ["Text", "Image"], #required
            default_index = 0, 
        )
        return selected


