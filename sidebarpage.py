from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu

def show():
    with st.sidebar:
         bg = """<div style='background-color:white; padding:13px'>
              <h1 style='color:black'>Sentiment Analysis  😊😐😕😡</h1>
       </div>"""
        st.markdown(bg, unsafe_allow_html=True)
        selected = option_menu(
            menu_title = "👇Select the type of Sentiment Analytics",
            options = ["Text", "Image"], #required
            default_index = 0, 
        )
        return selected
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             #background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             #background: content-box radial-gradient(#FF0000, white);
             background-color:#D8BFD8;
             background-attachment: fixed;
             background-size: contain;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
