from pickle import FALSE
import streamlit as st
import streamlit.components.v1 as components
#import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
"""
def show():
    with stx.tabs():
        st.code("import extra_streamlit_components as stx")
        selected = stx.tab_bar(data=[
            stx.TabBarItemData(id="Text", title="✍️ To Do", description="Tasks to take care of"),
            stx.TabBarItemData(id="Image", title="💔 Overdue", description="Tasks missed out"),], default=1)
        st.info(f"{selected=}")
        return selected
"""

def show(): 
    bg = """<body bgcolor="#800000"><div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Sentiment Analysis  😊😐😕😡</h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)
    #st.title("Sentiment Analysis  😊😐😕😡")
    selected = st.radio( "👇Select the type of Sentiment Analytics ", ("Text", "Image")) 
    return selected
