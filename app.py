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
            "trailer": "https://youtu.be/GVQGWgeVc4k?si=2Pv61CkbOHtVrlYS"
        },
        {
            "name": "Business Proposal",
            "poster": "/static/posters/bp.jpeg",
            "rating": 4.6,
            "trailer": "https://youtu.be/mh4R-WXRhQo?si=Bbd8a5cXd554-I7N"
        }
    ],
    "action": [
        {
            "name": "Vincenzo",
            "poster": "/static/posters/vincenzo.jpg",
            "rating": 4.8,
            "trailer": "https://youtu.be/_J8tYxYB_YU?si=BSGp5ApaKFs2Xj4T"
        },
        {
            "name": "Itaewon Class",
            "poster": "/static/posters/ic.jpg",
            "rating": 4.7,
            "trailer": "https://youtu.be/NNP8m3gaaFE?si=4kVcylGDKu4E07UE"
        }
    ],
    "comedy": [
        {
            "name": "Welcome to Waikiki",
            "poster": "/static/posters/wtw.jpeg",
            "rating": 4.5,
            "trailer": "https://youtu.be/AJ_eVJp-IuQ?si=cZYof0dzxrGlxOP_"
        },
        {
            "name": "Goblin",
            "poster": "/static/posters/goblin.jpeg",
            "rating": 4.9,
            "trailer": "https://youtu.be/8AcNEVUzV4o?si=gTnIdB0WB8AgUsN1"
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
