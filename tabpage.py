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
    st.title("Sentiment Analysis 😊😐😕😡")
    #components.html("""<hr style="height:1px;border:none;color:#333;background-color:#333; margin-bottom: 3px" /> """)
    selected = st.radio( "Select a tab", ("Text", "Image")) 
    return selected
