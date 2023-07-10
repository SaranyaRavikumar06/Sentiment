import streamlit as st
import sidebar
import textPage
import imageanalysispage
# st.title("Hello")
page = sidebar.show()

if page=="Text":
    textPage.renderPage()
elif page=="Image":
    imagePage.renderPage()
