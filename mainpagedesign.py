import streamlit as st
import sidebarpage
import textpage
import imageanalysis
page = sidebarpage.show()
if page=="Text":
    textpage.renderPage()
else:
    imageanalysis.renderPage()
