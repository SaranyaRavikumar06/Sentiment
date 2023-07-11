import streamlit as st
#import sidebarpage
import tabpage
import textpage
import imageanalysis
# st.title("Hello")
page = tabpage.show()
if page=="Text":
    textpage.renderPage()
elif page=="Image":
    imageanalysis.renderPage()
