import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("tmdb_5000_movies.csv")
movies = df[["title", "overview", "genres", "keywords"]].fillna("")
movies["combined"] = movies["overview"] + " " + movies["genres"] + " " + movies["keywords"]

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["combined"])
cosine_sim = cosine_similarity(tfidf_matrix)

def recommend_movie(title, num=5):
    if title not in movies["title"].values:
        return ["Movie not found in dataset."]
    idx = movies[movies["title"] == title].index[0]
    sim_scores = cosine_sim[idx]
    similar_idx = sim_scores.argsort()[-num-1:-1][::-1]
    return movies.iloc[similar_idx]["title"].tolist()

user_movie = input("Enter a movie name: ")
print("\nRecommended Movies:")
for rec in recommend_movie(user_movie, 5):
    print("-", rec)
