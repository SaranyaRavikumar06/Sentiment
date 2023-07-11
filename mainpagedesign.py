import streamlit as st
import sidebarpage
import textpage
import imageanalysis
# st.title("Hello")
page = sidebarpage.show()
if page=="Text":
    textpage.renderPage()
elif page=="Image":
    imageanalysis.renderPage()
