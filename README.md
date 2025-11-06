🎬 Movie Data ETL Pipeline
📘 Overview

This project builds an ETL (Extract, Transform, Load) pipeline using Python. The pipeline processes movie data from CSV files and enriches it with additional information from the OMDb API. Finally, it loads the cleaned and structured data into a relational database.

🧩 ETL Steps
1️⃣ Extract

Input Files:

movies.csv (Movie details)

ratings.csv (User ratings)

API Source: OMDb API

Each movie is enriched with metadata fetched using the movie title or IMDb ID.

Error Handling:

Logs cases where a movie cannot be found in the API.

Handles invalid or missing API responses gracefully.

2️⃣ Transform

Data Cleaning:

Handles missing values and incorrect data types.

Converts release dates to proper date formats.

Removes duplicates and trims extra spaces.

Data Enrichment:

Merges CSV data with API data using title or IMDb ID.

Adds fields such as Director, Genre, Runtime, and IMDb Rating.

Feature Engineering (Bonus):

Parses the genres column into a list or separate entries.

Creates a release_decade column (e.g., 1990s, 2000s, etc.).

3️⃣ Load

Destination: Relational Database (e.g., SQLite, PostgreSQL, or MySQL)

Process:

Loads the transformed dataset into structured tables (e.g., movies, ratings, movie_details).

Ensures idempotency — running the script multiple times won’t create duplicates.
🧰 Technologies Used

Python 3.x

Libraries:

pandas – Data manipulation

requests – API integration

sqlalchemy – Database connectivity

dotenv – Environment variable management

logging – Tracking errors and process steps
🚀 Future Improvements

Add unit tests for ETL components.

Implement parallel API calls for faster extraction.

Integrate a data visualization dashboard (e.g., Tableau, Power BI).
