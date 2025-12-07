
from sqlalchemy import create_engine, text

DB_URL = "mysql+pymysql://sql12810877:CjUfN1Tclg@sql12.freesqldatabase.com:3306/sql12810877"

engine = create_engine(DB_URL)

jobs = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    for row in result.all():
        jobs.append(dict(row._mapping))
