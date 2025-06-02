from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Your upgraded data (more K-Dramas per genre)
kdramas = {
    "romance": [
        {
            "name": "Crash Landing on You",
            "poster": "/static/posters/cloy.jpeg",
            "rating": 4.9,
            "trailer": "https://www.youtube.com/embed/GVQGWgeVc4k"
        },
        {
            "name": "Business Proposal",
            "poster": "/static/posters/bp.jpeg",
            "rating": 4.6,
            "trailer": "https://www.youtube.com/embed/mh4R-WXRhQo"
        }
    ],
    "action": [
        {
            "name": "Vincenzo",
            "poster": "/static/posters/vincenzo.jpg",
            "rating": 4.8,
            "trailer": "https://www.youtube.com/embed/_J8tYxYB_YU"
        },
        {
            "name": "Itaewon Class",
            "poster": "/static/posters/ic.jpg",
            "rating": 4.7,
            "trailer": "https://www.youtube.com/embed/NNP8m3gaaFE"
        }
    ],
    "comedy": [
        {
            "name": "Welcome to Waikiki",
            "poster": "/static/posters/wtw.jpeg",
            "rating": 4.5,
            "trailer": "https://www.youtube.com/embed/AJ_eVJp-IuQ"
        },
        {
            "name": "Goblin",
            "poster": "/static/posters/goblin.jpeg",
            "rating": 4.9,
            "trailer": "https://www.youtube.com/embed/8AcNEVUzV4o"
        }
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None
    if request.method == "POST":
        genre = request.form["genre"]
        recommendation = random.choice(kdramas.get(genre, []))
    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
