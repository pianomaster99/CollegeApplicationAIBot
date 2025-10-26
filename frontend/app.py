from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/essay")
def essay():
    return render_template("essay.html")

@app.route("/activities")
def activities():
    return render_template("activities.html")

@app.route("/honors")
def honors():
    return render_template("honors.html")

@app.route("/testing")
def testing():
    return render_template("testing.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/submit_essay", methods=["POST"])
def submit_essay():
    essay_text = request.form.get("essay_text")
    
    print("Received essay:", essay_text)
    return render_template("essay_received.html", response="Get a job")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)