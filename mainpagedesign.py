import streamlit as st
import sidebarpage
import textblobanalysis
import texttoemotion
import vader
page = sidebarpage.show()
if page=="Text2Emotion Analysis":
    texttoemotion.renderPage() 
elif page=="TextBlob Analysis":
    textblobanalysis.renderPage()
elif page=="VADER Sentiment Analysis":
    vader.renderPage()
