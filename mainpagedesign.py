import streamlit as st
import sidebarpage
import textblob
import texttoemotion
import vader
page = sidebarpage.show()
if page=="TextBlob Analysis":
    textblob.renderPage()
elif page=="Text2Emotion Analysis":
    texttoemotion.renderPage()
elif page=="VADER Sentiment Analysis":
    vader.renderPage()
