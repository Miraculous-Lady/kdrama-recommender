from flask import Flask, render_template, request
import random

app = Flask(__name__)

dramas = {
    "romance": ["Crash Landing on You", "Goblin", "True Beauty"],
    "thriller": ["Flower of Evil", "Stranger", "Vincenzo"],
    "comedy": ["Welcome to Waikiki", "Business Proposal", "Strong Woman Do Bong Soon"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = ""
    if request.method == "POST":
        mood = request.form["mood"]
        recommendation = random.choice(dramas.get(mood, []))
    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
