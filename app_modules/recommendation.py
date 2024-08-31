import pandas as pd
import pickle
import streamlit as st
from src.movie_recommendation_project.pipeline.movie_recommendation import PredictionPipeline

prediction_pipeline=PredictionPipeline()

def movie_recommendation():
    df=pd.read_csv("artifacts/data_transformation/tf_data.csv")
    st.write("Movie recommendation app!")
    selected_movie=st.selectbox("Select Movie",df["title"])
    with open('artifacts/model_building/recommender_model.pkl', 'rb') as file:
            similarity = pickle.load(file)

    l=[]
    index = df[df['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:7]:
        l.append(df.iloc[i[0]].title)

    col1,col2=st.columns([1,2])
    image_url=df[df["title"]==selected_movie]["img_link"].values[0]


    with col1:
         st.image(image_url,width=150)

    with col2:
         st.write("[{}]({})".format(df[df["title"]==selected_movie]["title"].values[0],df[df["title"]==selected_movie]["link"].values[0]))
         st.write(df[df["title"]==selected_movie]["plot"].values[0])
         st.write("{} , {}".format(df[df["title"]==selected_movie]["genre"].values[0],df[df["title"]==selected_movie]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==selected_movie]["rating"].values[0]))

    st.write("You may also like...")
    col1,col2,col3=st.columns(3)
    image_url0=df[df["title"]==l[0]]["img_link"].values[0]
    image_url1=df[df["title"]==l[1]]["img_link"].values[0]
    image_url2=df[df["title"]==l[2]]["img_link"].values[0]


    with col1:
         st.image(image_url0,width=150)
         st.write("[{}]({})".format(df[df["title"]==l[0]]["title"].values[0],df[df["title"]==l[0]]["link"].values[0]))
         st.write("{} , {}".format(df[df["title"]==l[0]]["genre"].values[0],df[df["title"]==l[0]]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==l[0]]["rating"].values[0]))

    with col2:
         st.image(image_url1,width=150)
         st.write("[{}]({})".format(df[df["title"]==l[1]]["title"].values[0],df[df["title"]==l[1]]["link"].values[0]))
         st.write("{} , {}".format(df[df["title"]==l[1]]["genre"].values[0],df[df["title"]==l[1]]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==l[1]]["rating"].values[0]))

    with col3:
         st.image(image_url2,width=150)
         st.write("[{}]({})".format(df[df["title"]==l[2]]["title"].values[0],df[df["title"]==l[2]]["link"].values[0]))
         st.write("{} , {}".format(df[df["title"]==l[2]]["genre"].values[0],df[df["title"]==l[2]]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==l[2]]["rating"].values[0]))

    col1,col2,col3=st.columns(3)
    image_url3=df[df["title"]==l[3]]["img_link"].values[0]
    image_url4=df[df["title"]==l[4]]["img_link"].values[0]
    image_url5=df[df["title"]==l[5]]["img_link"].values[0]

    with col1:
         st.image(image_url3,width=150)
         st.write("[{}]({})".format(df[df["title"]==l[3]]["title"].values[0],df[df["title"]==l[3]]["link"].values[0]))
         st.write("{} , {}".format(df[df["title"]==l[3]]["genre"].values[0],df[df["title"]==l[3]]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==l[3]]["rating"].values[0]))

    with col2:
         st.image(image_url4,width=150)
         st.write("[{}]({})".format(df[df["title"]==l[4]]["title"].values[0],df[df["title"]==l[4]]["link"].values[0]))
         st.write("{} , {}".format(df[df["title"]==l[4]]["genre"].values[0],df[df["title"]==l[4]]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==l[4]]["rating"].values[0]))

    with col3:
         st.image(image_url5,width=150)
         st.write("[{}]({})".format(df[df["title"]==l[5]]["title"].values[0],df[df["title"]==l[5]]["link"].values[0]))
         st.write("{} , {}".format(df[df["title"]==l[5]]["genre"].values[0],df[df["title"]==l[5]]["year"].values[0]))
         st.write("Rating: {}".format(df[df["title"]==l[5]]["rating"].values[0]))

    


    