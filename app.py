from flask import Flask, render_template, jsonify
from flask import jsonify

app = Flask(__name__)

jobs = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'          
},
{
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
},
{
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
},
{
    'id': 4,
    'title': 'Full Stack Developer',
    'location': 'Austin, USA',
    'salary': '$120,000'
},
{
    'id': 5,
    'title': 'Data Analyst',
    'location': 'New York, USA',
    'salary': '$100,000'
}]

@app.route("/")
def hello_world():
    return render_template("index.html", jobs = jobs)
@app.route("/api/jobs")
def jobsapi():
    return jsonify(jobs)

app.run(debug=True)
