import streamlit as st
import Sidebarpage
import textpage
import imageanalysis
# st.title("Hello")
page = Sidebarpage.show()

if page=="Text":
    textpage.renderPage()
elif page=="Image":
    imageanalysis.renderPage()
