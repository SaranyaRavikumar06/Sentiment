import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()

def plotPie(labels, values):
    fig = go.Figure(
        go.Pie(
        labels = labels,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig)

    
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

def getSentiments(userText, type):
    if(type == 'Positive/Negative/Neutral - TextBlob'):
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
    elif('type == Positive/Negative/Neutral -VADER'):
        scores = SentimentIntensityAnalyzer().polarity_scores(text)
        if scores['compound'] >= 0.05 :
            image = Image.open('./images/positive.PNG')
        elif scores['compound'] <= - 0.05 :
            image = Image.open('./images/negative.PNG')
        else :
            image = Image.open('./images/neutral.PNG')
        col1, col2, col3,col4 = st.columns(4)
        col1.metric("Positive Score", scores['pos'], None)
        col2.metric("Negative Score", scores['neg'], None)
        col3.metric("Neutral Score", scores['neu'], None)
        col4.metric("Compound Score", scores['compound'], None)
        st.image(image, caption=status)
    elif(type == 'Happy/Sad/Angry/Fear/Surprise - text2emotion'):
        emotion = dict(te.get_emotion(userText))
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Happy 😊", emotion['Happy'], None)
        col2.metric("Sad 😔", emotion['Sad'], None)
        col3.metric("Angry 😠", emotion['Angry'], None)
        col4.metric("Fear 😨", emotion['Fear'], None)
        col5.metric("Surprise 😲", emotion['Surprise'], None)
        plotPie(list(emotion.keys()), list(emotion.values()))
        

def renderPage():
    st.subheader("User Input Text Analysis")
    st.text("Analyzing text data given by the user and find sentiments within it.")
    st.text("")
    userText = st.text_input('User Input', placeholder='Input text HERE')
    st.text("")
    type = st.selectbox(
     'Type of analysis',
     ('Positive/Negative/Neutral - TextBlob','Positive/Negative/Neutral -VADER', 'Happy/Sad/Angry/Fear/Surprise - text2emotion'))
    st.text("")
    if st.button('Predict'):
        if(userText!="" and type!=None):
            st.text("")
            st.components.v1.html("""
                                <h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>
                                """, height=100)
            getSentiments(userText, type)


