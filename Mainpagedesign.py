import streamlit as st
import sidebar
import textpage
import imageanalysis
# st.title("Hello")
page = sidebar.show()

if page=="Text":
    textpage.renderPage()
elif page=="Image":
    imageanalysis.renderPage()
