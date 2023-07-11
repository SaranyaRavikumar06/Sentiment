from pickle import FALSE
import streamlit as st
import streamlit.components.v1 as components
#import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
def show(): 
    bg = """<body bgcolor="#DBF9FC"><div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Sentiment Analysis  😊😐😕😡</h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)
    selected = st.radio( "👇Select the type of Sentiment Analytics ", ("Text", "Image")) 
    return selected
