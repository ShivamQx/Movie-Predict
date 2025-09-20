from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

df = pd.read_csv("concated.csv")
movies = df[["title", "overview", "genres", "keywords"]].fillna("")
movies["combined"] = (
    movies["overview"] + " " + movies["genres"] + " " + movies["keywords"]
)
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["combined"])
cosine_sim = cosine_similarity(tfidf_matrix)


def recommend_movie(title, num=5):
    if title not in movies["title"].values:
        return []
    idx = movies[movies["title"] == title].index[0]
    sim_scores = cosine_sim[idx]
    similar_idx = sim_scores.argsort()[-num - 1 : -1][::-1]

    recs = []
    for i in similar_idx:
        recs.append({
            "title": movies.iloc[i]["title"],
            "overview": movies.iloc[i]["overview"] or "No overview available.",
            "genre": movies.iloc[i]["genres"]
        })
    return recs

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_movie = request.form.get("movie")
        recs = recommend_movie(user_movie, 6)
        return render_template("result.html", title=user_movie, recs=recs)

    # Only send movie titles for fast load
    movie_titles = movies["title"].tolist()
    return render_template("index.html", movies=movie_titles)

if __name__ == "__main__":
    app.run(debug=True)
