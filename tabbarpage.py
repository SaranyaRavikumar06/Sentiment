from pickle import FALSE
import streamlit as st
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
def show():
    st.code("import extra_streamlit_components as stx")
    selected = stx.tab_bar(data=[
        stx.TabBarItemData(id="Text", title="✍️ Text Data", description="Tasks to take care of"),
        stx.TabBarItemData(id="Image", title="💔 Image", description="Tasks missed out")])
    return selected
