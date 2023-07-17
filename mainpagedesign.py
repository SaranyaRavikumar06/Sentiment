import streamlit as st
import sidebarpage
import textblob
import texttoemotion
import vader
page = sidebarpage.show()
if page=="Text2Emotion Analysis":
    texttoemotion.renderPage() 
elif page=="TextBlob Analysis":
    textblob.input()
elif page=="VADER Sentiment Analysis":
    vader.renderPage()
