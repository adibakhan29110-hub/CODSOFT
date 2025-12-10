from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies dataset
movies = pd.read_csv("data/movies.csv")

# Process data
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies["tags"])
similarity = cosine_similarity(count_matrix)

app = Flask(__name__)

def recommend(movie_name):
    movie_name = movie_name.lower()
    if movie_name not in movies["title"].str.lower().values:
        return ["Movie not found in database"]

    idx = movies[movies["title"].str.lower() == movie_name].index[0]
    distances = list(enumerate(similarity[idx]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    return [movies.iloc[i[0]].title for i in movies_list]


@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = recommend(movie)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
