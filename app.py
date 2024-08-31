import os 
import streamlit as st
import pandas as pd
from app_modules.recommendation import movie_recommendation
from app_modules.analytics import movie_analysis




def home():
    st.title("Movie recommendation app!")
    st.write("Discover your next favorite movie with our advanced Movie Recommender System! This app uses cosine-similarity machine learning techniques to suggest movies tailored to your tastes. Whether you're in the mood for a blockbuster hit, a critically acclaimed indie, or something in between, we've got you covered.")
    st.write("Below button will train the model from scratch, from data ingestion to data transformation to model building")
    st.write("|||***Try at your own risk***|||")

    if st.button("Train Model"):
        os.system("python main.py")




def analytics_module():
    st.title("Movies Data Analysis!")
    ma=movie_analysis()
    ma.grp_by_director()
    ma.rating_director()
    input_x=st.selectbox("select column to see the distribution",["rating","runtime","gross"])
    ma.dist_plot(input_x)
    input_y=st.selectbox("select column for descriptive stats",["rating","runtime","gross"])
    ma.desc(input_y)



# Sidebar with navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Movie Recommendation", "Analytics Module"])

# Display the selected page
if page == "Home":
    home()
elif page == "Movie Recommendation":
    movie_recommendation()
elif page == "Analytics Module":
    analytics_module()
