# 🎬 Movie ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline using **MovieLens CSV data** and the **OMDb API**.

---

## 🚀 Features
- Reads `movies.csv` and `ratings.csv` from MovieLens
- Fetches additional data (Director, Plot, Box Office) from the OMDb API
- Cleans and merges all data
- Loads final data into an SQLite database
- Includes SQL queries for analysis

---

## 🛠️ Setup Instructions

### 1. Install dependencies
```bash
pip install pandas requests
