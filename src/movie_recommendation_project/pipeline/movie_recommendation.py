from src.movie_recommendation_project.config.configuration import ConfigurationManager
import pickle


class PredictionPipeline:
    def __init__(self):
        self.config =ConfigurationManager().get_model_building_config()
        self.df=self.config.data_path

    

    def recommend(self,movie):
        l=[]
        with open('artifacts/model_building/recommender_model.pkl', 'rb') as file:
            similarity = pickle.load(file)
        index = self.df[self.df['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            l.append(self.df.iloc[i[0]].title)
        return l
