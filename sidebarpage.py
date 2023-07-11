from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu

def show():
    bg = """<div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Sentiment Analysis  😊😐😕😡</h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)
    with st.sidebar:
        selected = option_menu(
            menu_title = "👇Select the type of Sentiment Analytics",
            options = ["None","Text", "Image"], #required
            default_index = 0, 
        )
        return selected
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color:#1e3d59;
             background-attachment: fixed;
             background-size: contain;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
