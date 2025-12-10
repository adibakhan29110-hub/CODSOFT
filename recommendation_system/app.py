import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("data/movies.csv")

# Combine features
movies["combined"] = (
    movies["title"] + " " +
    movies["genres"] + " " +
    movies["description"]
)

# Convert to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["combined"])

# Calculate similarity
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(movie_title):
    if movie_title not in movies["title"].values:
        return ["Movie not found in database"]

    idx = movies[movies["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i, score in sorted_scores:
        recommendations.append(movies.iloc[i]["title"])

    return recommendations

# Test
if __name__ == "__main__":
    movie = input("Enter a movie name: ")
    print("\nRecommended movies:")
    for m in recommend(movie):
        print(" -", m)
