from flask import Flask, render_template, jsonify
from flask import jsonify
from database import load_jobs, load_jobs_by_id

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", jobs = load_jobs())


@app.route("/job/<id>")
def open_job(id):
    job = load_jobs_by_id(id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job = job)

@app.route("/api/jobs")
def jobsapi():
    return jsonify(jobs)

app.run(host="0.0.0.0", debug=True)
