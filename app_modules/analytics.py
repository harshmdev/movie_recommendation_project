import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#Gross by director
#rating by director
#Distribution of rating,gross,runtime
#relation between runtime,rating,gross
#descriptive statistics of runtime, gross, rating

class movie_analysis:
    def __init__(self):
        self.df=pd.read_csv("artifacts/data_transformation/tf_data.csv")

    def grp_by_director(self):
        temp_df=self.df.groupby("director")["gross"].mean().sort_values(ascending=False).reset_index()
        fig, ax = plt.subplots()
        sns.barplot(data=temp_df.head(10), x="director", y="gross", ax=ax)
        
        # Set the title and labels
        ax.set_title('Average Gross Earnings by Director')
        ax.set_xlabel('Director Name')  # Change the x-axis title
        ax.set_ylabel('Average Gross Earnings (100 Million)')
        
        # Rotate the x-ticks for better readability
        plt.xticks(rotation=45, ha='right')
        
        # Display the plot in Streamlit
        st.pyplot(fig)

    def rating_director(self):
        temp_df=self.df.groupby("director")["rating"].sum().sort_values(ascending=False).reset_index()
        fig,ax=plt.subplots()
        sns.barplot(data=temp_df.head(10),x="director",y="rating",ax=ax)
        ax.set_title('Sum of Ratings by Director')
        ax.set_xlabel('Director Name')  # Change the x-axis title
        ax.set_ylabel('Sum of Ratings')

        # Rotate the x-ticks for better readability
        plt.xticks(rotation=45, ha='right') 
        st.pyplot(fig)

    def dist_plot(self,x):
        fig,ax=plt.subplots()
        sns.histplot(self.df,x=self.df[x],kde=True,ax=ax)
        ax.set_xlabel("{}".format(x))
        st.pyplot(fig)

    def desc(self,x):
        st.write(self.df[x].describe())