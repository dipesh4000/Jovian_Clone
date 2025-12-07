from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import json
import os
import markdown

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL)
jobs = []
def load_jobs_from_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs"))
            jobs = [dict(row._mapping) for row in result.all()]
        return jobs
    except Exception as e:
        print(f"Error loading jobs from database: {e}")
        return []

def load_jobs_from_json():
    try:
        with open("jobs.json", 'r') as f:
            return json.load(f)
    except:
        return []
def save_jobs_from_db(jobs):
    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

def load_jobs():
    jobs = load_jobs_from_db()
    if jobs:
        save_jobs_from_db(jobs)
    else:
        jobs = load_jobs_from_json()
    return jobs

def load_jobs_by_id(id):
    jobs = load_jobs()
    for job in jobs:
        if job["id"] == int(id):
            job["responsibilities"] = markdown.markdown(job["responsibilities"])
            job["requirements"] = markdown.markdown(job["requirements"])    
            return job
    return None