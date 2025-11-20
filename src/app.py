from flask import Flask, request, Response, render_template
import json
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Load JSON data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOVIES_PATH = os.path.join(BASE_DIR, "assets", "movies.json")

with open(MOVIES_PATH) as f:
    movies = json.load(f)

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/movies")
def get_movies():
    reordered = [
        {
            "Position": movie["Position"],
            "Title": movie["Title"],
            "IMDb Rating": movie["IMDb Rating"],
            "MPAA Rating": movie["MPAA Rating"],
            "Genres": movie["Genres"]
        }
        for movie in movies
    ]
    return Response(json.dumps(reordered, indent=2), mimetype='application/json')


@app.route("/search")
def search_movie():
    title_query = request.args.get("title", "").lower()
    genre_query = request.args.get("genre", "").lower()
    rating_query = request.args.get("rating", "")
    mpaa_query = request.args.get("mpaa", "") 

    filtered = []

    for movie in movies:
        title_match = title_query in movie["Title"].lower() if title_query else True
        genre_match = genre_query in movie["Genres"].lower() if genre_query else True
        rating_match = float(movie["IMDb Rating"]) >= float(rating_query) if rating_query else True
        mpaa_match = movie["MPAA Rating"] == mpaa_query if mpaa_query else True

        if title_match and genre_match and rating_match and mpaa_match:
            filtered.append({
                "Position": movie["Position"],
                "Title": movie["Title"],
                "IMDb Rating": movie["IMDb Rating"],
                "MPAA Rating": movie["MPAA Rating"],
                "Genres": movie["Genres"]
            })

    return Response(json.dumps(filtered, indent=2), mimetype='application/json')


@app.route("/genres")
def get_genres():
    """Return a unique sorted list of all genres."""
    all_genres = set()
    for movie in movies:
        for g in movie["Genres"].split(","):
            all_genres.add(g.strip())
    genres_sorted = sorted(all_genres)
    return Response(json.dumps(genres_sorted, indent=2), mimetype='application/json')


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)