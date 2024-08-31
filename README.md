# Movie Recommender System

Welcome to the Movie Recommender System! This project is designed to help users discover movies that match their preferences by leveraging machine learning techniques. The app offers personalized recommendations based on various movie features such as genres, directors, stars, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Modeling Approach](#modeling-approach)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Personalized Movie Recommendations**: Suggest movies based on your selection of movie.
- **Trend Analysis**: Explore trends across years, genres, and directors to understand the evolution of the movie industry.
- **Top Lists**: Discover top-rated and highest-grossing movies.
- **Interactive Interface**: User-friendly interface with interactive elements and visualizations.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/harshmdev/movie_recommendation_project.git
    cd movie_recommendation_project
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```
5. **Train the model**
    on homepage there is a button called train model click on it to train the model.

## Usage

1. After running the Streamlit app, navigate to the provided local URL in your web browser.
2. On the home page, you can read about the app’s features and how it works.
3. Use the recommendation feature to get movie suggestions based on your preferences.
4. Explore trends, top lists, and more by navigating through the different sections of the app.

## Dataset

The dataset used in this project contains information on movies, including:

- **Title**
- **Rating**
- **Runtime**
- **Genre**
- **Metascore**
- **Plot**
- **Director**
- **Stars**
- **Vote Count**
- **Gross Earnings**
- **Year of Release**
- **Writer**
- **Image Link**

Data was sourced from [IMDb](https://www.imdb.com/) .

## Modeling Approach

The recommendation system combines several machine learning techniques:

- **CountVectorizer** for text-based features like genres, directors, stars, etc.
- **Word2Vec** for plot analysis.
- **MinMaxScaler** for normalizing numerical features like the year of release.
- **Cosine Similarity**  for calculating similarities between movies.

## Deployment

The project can be deployed using Docker. Here's how you can do it:

1. **Build the Docker image**:
    ```bash
    docker build -t movie-recommender .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 8501:8501 movie-recommender
    ```

3. **Access the app** by navigating to `http://localhost:8501` in your web browser.

4. **Pull the docker image** i already deploy it on docker "harshmdev/movie_recommendation:01" to pull it 
    ```bash
    docker pull harshmdev/movie_recommendation:01
    ```

## Future Improvements

- **User-Based Collaborative Filtering**: Incorporate user data to improve the accuracy of recommendations.
- **Real-Time Recommendations**: Update the recommendation engine to provide real-time suggestions based on ongoing user interactions.
- **Enhanced Visualizations**: Add more sophisticated visualizations to analyze movie trends and data.
- **Integration with External APIs**: Fetch the latest movie data dynamically from external APIs like TMDb or IMDb.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your proposed changes.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.
