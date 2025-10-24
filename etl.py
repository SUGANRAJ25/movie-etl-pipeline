import pandas as pd
import requests
import sqlite3
import time
conn = sqlite3.connect("movies.db")
cur = conn.cursor()
cur.executescript(open("schema.sql", "r").read())
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
API_KEY = "d3bd3e2e"  
OMDB_URL = "http://www.omdbapi.com/"

def fetch_omdb_data(title):
    try:
        params = {"t": title, "apikey": API_KEY}
        r = requests.get(OMDB_URL, params=params)
        data = r.json()
        if data.get("Response") == "True":
            return {
                "Director": data.get("Director"),
                "Plot": data.get("Plot"),
                "BoxOffice": data.get("BoxOffice"),
                "Year": data.get("Year")
            }
        else:
            return None
    except:
        return None


movie_data = []
for _, row in movies.iterrows():
    extra = fetch_omdb_data(row['title'])
    if extra:
        movie_data.append({
            "movieId": row['movieId'],
            "title": row['title'],
            "genres": row['genres'],
            "director": extra["Director"],
            "plot": extra["Plot"],
            "box_office": extra["BoxOffice"],
            "year": extra["Year"]
        })
    else:
        movie_data.append({
            "movieId": row['movieId'],
            "title": row['title'],
            "genres": row['genres'],
            "director": None,
            "plot": None,
            "box_office": None,
            "year": None
        })
    time.sleep(0.3) 

movies_df = pd.DataFrame(movie_data)

movies_df.to_sql("movies", conn, if_exists="replace", index=False)
ratings.to_sql("ratings", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("ETL process completed successfully!")
