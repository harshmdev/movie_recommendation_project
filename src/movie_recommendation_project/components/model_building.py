import pandas as pd
import numpy as np
from src.movie_recommendation_project.entity import ModelBuildingConfig
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import pickle


class ModelBuilding:
    def __init__(self,config: ModelBuildingConfig):
        self.config=config
        self.df=pd.read_csv(config.data_path)

    def model_builder(self):
        plot_sentences = [plot.split() for plot in self.df['plot']]
        word2vec_model = Word2Vec(sentences=plot_sentences, vector_size=100, window=5, min_count=1)
        plot_vectors = np.array([np.mean([word2vec_model.wv[word] for word in words], axis=0) for words in plot_sentences])

        # 1. CountVectorizer on genre, director, star and writer
        # Initialize separate CountVectorizer instances for each column
        genre_vectorizer = CountVectorizer()
        director_vectorizer = CountVectorizer()
        star_vectorizer = CountVectorizer()
        writer_vectorizer = CountVectorizer()
        scaler=MinMaxScaler()

        # Vectorize each categorical column separately
        genre_vectors = genre_vectorizer.fit_transform(self.df['genre']).toarray()
        director_vectors = director_vectorizer.fit_transform(self.df['director']).toarray()
        star_vectors = star_vectorizer.fit_transform(self.df['star']).toarray()
        writer_vectors = writer_vectorizer.fit_transform(self.df['writer']).toarray()

        # Scale the numerical 'year' column
        year_scaled = scaler.fit_transform(self.df[['year']])

        combined_vectors = np.hstack((plot_vectors,genre_vectors, director_vectors, star_vectors, writer_vectors, year_scaled))
        similarity = cosine_similarity(combined_vectors)

        pickle.dump(similarity,open(self.config.model_path,"wb"))

