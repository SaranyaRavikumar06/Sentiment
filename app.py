import streamlit as st
import sidebar
import textpage
import imageanalysis
# import videoPage
# import twitterAnalysisPage

# st.title("Hello")
page = sidebar.show()

if page=="Text":
    textPage.renderPage()
# elif page=="Audio":
#     audioPage.renderPage()
elif page=="IMDb movie reviews":
    imdbReviewsPage.renderPage()
elif page=="Image":
    imagePage.renderPage()
# elif page=="Video":
#     videoPage.main()
# elif page=="Twitter Data":
#     twitterAnalysisPage.renderPage()
