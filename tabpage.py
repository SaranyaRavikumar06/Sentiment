from pickle import FALSE
import streamlit as st
import streamlit.components.v1 as components
#import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
def show(): 
    st.title("Sentiment Analysis  😊😐😕😡")
    selected = st.radio( "👇Select the type of Sentiment Analytics ", ("Text", "Image")) 
    return selected
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             #background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background: content-box radial-gradient(crimson, skyblue);
             #background-color:aquamarine;
             background-attachment: fixed;
             background-size: contain;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
