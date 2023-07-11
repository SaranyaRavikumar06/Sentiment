from pickle import FALSE
import streamlit as st
import streamlit.components.v1 as components
#import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
def show(): 
   st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://cdn-media-1.freecodecamp.org/images/1*TdiVdPnYkvgl3qWnLGgOcg.jpeg");
    }
   </style>
    """,
    unsafe_allow_html=True
    )
    #st.markdown(bg, unsafe_allow_html=True)
    st.title("Sentiment Analysis  😊😐😕😡")
    selected = st.radio( "👇Select the type of Sentiment Analytics ", ("Text", "Image")) 
    return selected
