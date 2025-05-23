from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
REVIEWS_PATH = "data/reviews.json"

@app.route("/")
def index():
    with open("data/profile.json", "r") as f:
        profile = json.load(f)
    with open(REVIEWS_PATH, "r") as f:
        reviews = json.load(f)
    return render_template("index.html", profile=profile, reviews=reviews)

@app.route("/submit_review", methods=["POST"])
def submit_review():
    author = request.form.get("author")
    text = request.form.get("text")
    stars = int(request.form.get("stars", 5))
    if author and text:
        new_review = {
            "author": author,
            "stars": stars,
            "text": text
        }
        if os.path.exists(REVIEWS_PATH):
            with open(REVIEWS_PATH, "r") as f:
                reviews = json.load(f)
        else:
            reviews = []
        reviews.insert(0, new_review)
        with open(REVIEWS_PATH, "w") as f:
            json.dump(reviews, f, ensure_ascii=False, indent=2)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/admin")
def admin_panel():
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)
    return render_template("admin.html", reviews=reviews)


from werkzeug.utils import secure_filename

@app.route("/upload_photo", methods=["POST"])
def upload_photo():
    photo = request.files.get("photo")
    if photo:
        filename = secure_filename("avatar.png")
        path = os.path.join("static", filename)
        photo.save(path)
    return redirect("/")


from utils.top import top_masters

@app.route("/admin")
def admin_panel():
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)
    top = top_masters()
    return render_template("admin.html", reviews=reviews, top=top)


from utils.stats import fake_activity_stats

@app.route("/admin")
def admin_panel():
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)
    top = top_masters()
    stats = fake_activity_stats()
    return render_template("admin.html", reviews=reviews, top=top, stats=stats)


from utils.block import get_blocked_masters

@app.route("/admin")
def admin_panel():
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)
    top = top_masters()
    stats = fake_activity_stats()
    blocked = get_blocked_masters()
    return render_template("admin.html", reviews=reviews, top=top, stats=stats, blocked=blocked)


@app.route("/client")
def client_panel():
    with open("data/client_data.json", "r") as f:
        data = json.load(f)
    return render_template("client.html", data=data)
