from pickle import FALSE
import streamlit as st
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
def show():
    with st.tabs():
        st.code("import extra_streamlit_components as stx")
        selected = stx.tab_bar(data=[
            stx.TabBarItemData(id="Text", title="✍️ To Do", description="Tasks to take care of"),
            stx.TabBarItemData(id="Image", title="💔 Overdue", description="Tasks missed out"),], default=1)
        st.info(f"{selected=}")
        return selected

