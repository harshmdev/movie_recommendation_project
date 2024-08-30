import pandas as pd
import ast
from src.movie_recommendation_project.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config=config
        self.df=pd.read_csv(self.config.data_path)


    def str_lst(self,x):
        return ast.literal_eval(x)
    
    def prepare_list(self,x):
        l=[]
        for i in x:
            l.append(i.lower().replace(" ",""))
        return " ".join(l)
    
    def puntuation_remover(self,x):
        punc = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        for ele in x:
            if ele in punc:
                x = x.replace(ele, " ")
        return x
    
    def prepare_words(self,x):
        l=[]
        ls=x.split(" ")
        for i in ls:
            l.append(i.lower())
        return " ".join(l)
    
    def transform_data(self):
        self.df.drop("ID",axis=1,inplace=True)
        new_names={
                    "Movie Name":"title",
                    "Rating":"rating",
                    "Votes":"vote",
                    "Directors":"director",
                    "Stars":"star",
                    "Metascore":"metascore",
                    "Genre":"genre",
                    "Plot":"plot",
                    "Runtime":"runtime",
                    "Gross":"gross",
                    "Link":"link"

                }
        self.df.rename(columns=new_names,inplace=True)

        self.df["runtime"]=self.df["runtime"].str.replace(" min","")
        self.df["genre"]=self.df["genre"].str.split(",")

        self.df["director"]=self.df["director"].apply(self.str_lst)
        self.df["star"]=self.df["star"].apply(self.str_lst)
        self.df["director"]=[i[0] for i in self.df["director"]]
        self.df["star"][287]=["Sara Cushman", "Don Hertzfeldt"]

        self.df.drop([13,27],inplace=True)
        self.df.reset_index(drop=True,inplace=True)

        self.df["year"]=self.df["year"].astype(str)
        self.df=self.df[self.df["year"].str.isdigit()]
        self.df["year"]=self.df["year"].astype(int)
        self.df=self.df[self.df["year"]>1800]

        self.df["writer"]=self.df["writer"].apply(self.str_lst)

        for col in ["genre","star","writer"]:
            self.df[col]=self.df[col].apply(self.prepare_list)

        self.df["plot"]=self.df["plot"].apply(self.puntuation_remover)

        self.df["director"]=self.df["director"].str.replace(" ","").str.lower()

        self.df["plot"]=self.df["plot"].apply(self.prepare_words)

        self.df.to_csv(self.config.transformed_data_path,index=False)
