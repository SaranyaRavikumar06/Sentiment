import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def getPolarity(userText):
    tb = TextBlob(userText)
    polarity = round(tb.polarity, 2)
    subjectivity = round(tb.subjectivity, 2)
    if polarity>0:
        return polarity, subjectivity, "Positive"
    elif polarity==0:
        return polarity, subjectivity, "Neutral"
    else:
        return polarity, subjectivity, "Negative"

def getSentiments(userText):
    polarity, subjectivity, status = getPolarity(userText)
    if(status=="Positive"):
        image = Image.open('./images/positive.PNG')
    elif(status == "Negative"):
        image = Image.open('./images/negative.PNG')
    else:
        image = Image.open('./images/neutral.PNG')
    col1, col2, col3 = st.columns(3)
    col1.metric("Polarity", polarity, None)
    col2.metric("Subjectivity", subjectivity, None)
    col3.metric("Result", status, None)
    st.image(image, caption=status)
    
def renderPage():
    st.subheader("User Input Text Analysis")
    st.text("Analyzing text data given by the user and find sentiments within it.")
    st.text("")
    userText = st.text_input('User Input', placeholder='Input text HERE')
    st.text("")
    if st.button('Predict'):
        if(userText!=""):
            st.text("")
            st.components.v1.html("""<h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>""", height=100)
            getSentiments(userText)
