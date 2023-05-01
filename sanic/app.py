import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from sanic import Sanic, json


load_dotenv()


DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))


app = Sanic(name=__name__) 

conn = psycopg2.connect(f"dbname='{DB_NAME}' user='{DB_USER}' host='{DB_HOST}' password='{DB_PASSWORD}'")


@app.route("/countries/")
def list_countries(request):
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM countries")
    # cur.execute("SELECT json_agg(countries) FROM countries")
    countries = cur.fetchall()
    return json(countries)


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, access_log=False, workers=10)