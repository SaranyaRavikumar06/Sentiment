from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu
def show():
    st.code("import extra_streamlit_components as stx")
    selected = st.tab_bar(data=[
        st.TabBarItemData(id="Text", title="✍️ Text Data", description="Tasks to take care of"),
        st.TabBarItemData(id="Image", title="💔 Image", description="Tasks missed out")])
    return selected
