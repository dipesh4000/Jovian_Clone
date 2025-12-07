from flask import Flask, render_template, jsonify
from flask import jsonify
from database import jobs

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", jobs = jobs)
@app.route("/api/jobs")
def jobsapi():
    return jsonify(jobs)

app.run(host="0.0.0.0", debug=True)
