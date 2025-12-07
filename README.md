
# Jovian_Clone

A simple Flask-based web application that serves as a clone project for job listing portals.

## Features

- Home page that displays jobs loaded from a database.
- REST API endpoint to retrieve job data as JSON.
- Database interaction using SQLAlchemy.
- Configuration using environment variables (.env).
- Simple deployment-ready structure (includes Gunicorn in requirements).

## Getting Started

### Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

#### `requirements.txt`
```text
Flask
sqlalchemy
pymysql
gunicorn
```

### Environment Variables

Create a `.env` file in the root directory with your database URL:

```
DB_URL=<your_database_url>
```

### Project Structure

```
├── app.py
├── database.py
├── requirements.txt
├── templates/
├── static/
└── .env
```

### Files

#### `app.py`
```python
from flask import Flask, render_template, jsonify
from flask import jsonify
from database import load_jobs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", jobs = load_jobs())

@app.route("/api/jobs")
def jobsapi():
    return jsonify(jobs)

app.run(host="0.0.0.0", debug=True)
```

#### `database.py`
```python
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL)

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs
```

## Usage

Start the application locally:

```bash
python app.py
```

- Visit `http://localhost:5000/` for the web interface.
- Visit `http://localhost:5000/api/jobs` for the JSON API endpoint (noting that the jobs variable must be available; see code for possible adjustments).

## Templates & Static Files

- Place your HTML templates in the `templates/` folder.
- Place images, CSS, and JS files in the `static/` folder.

*This project is for educational/demo purposes and mimics a basic jobs portal backend.*

