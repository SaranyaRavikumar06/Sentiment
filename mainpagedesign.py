import streamlit as st
#import sidebarpage
import tabbarpage
import textpage
import imageanalysis
# st.title("Hello")
page = tabbarpage.show()
if page=="Text":
    textpage.renderPage()
elif page=="Image":
    imageanalysis.renderPage()
