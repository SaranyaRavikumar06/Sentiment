import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

def getVaderscore(userText):
    vd = SentimentIntensityAnalyzer().polarity_scores(userText)
    compoundscore = vd['compound'] 
    positivescore=vd['pos'] 
    negativescore=vd['neg'] 
    neutralscore=vd['neu'] 
    if compoundscore >= 0.05 :
        return compoundscore, positivescore,"Positive"
    elif compoundscore <= - 0.05 :
        return compoundscore, negativescore,"Negative"
    else:
        return compoundscore, neutralscore,"Neutral"


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
        compoundscore1,vadermaxscore1,status1 = getVaderscore(userText)
        if(status1=="Positive"):
            image1 = Image.open('./images/positive.PNG')
        elif(status1 == "Negative"):
            image1 = Image.open('./images/negative.PNG')
        else:
            image1 = Image.open('./images/neutral.PNG')
        col1, col2, col3= st.columns(3)
        col1.metric("Compound Score",compoundscore1, None)
        col2.metric("VaderMaximum(Positive/Negative) Score",vadermaxscore1 , None)
        col3.metric("Result",status1, None)
        st.image(image1, caption=status1)
        
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
    type = st.selectbox('Type of analysis',('Positive/Negative/Neutral - TextBlob','Positive/Negative/Neutral -V ADER','Happy/Sad/Angry/Fear/Surprise - text2emotion'))
    st.text("")
    if st.button('Predict'):
        if(userText!="" and type!=None):
            st.text("")
            st.components.v1.html("""<h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>""", height=100)
            getSentiments(userText,type)


