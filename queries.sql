-- 1. Which movie has the highest average rating?
SELECT m.title, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.title
ORDER BY avg_rating DESC
LIMIT 1;

-- 2. Top 5 genres with the highest average rating
SELECT m.genres, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.genres
ORDER BY avg_rating DESC
LIMIT 5;

-- 3. Director with the most movies
SELECT director, COUNT(*) AS movie_count
FROM movies
WHERE director IS NOT NULL
GROUP BY director
ORDER BY movie_count DESC
LIMIT 1;

-- 4. Average rating per release year
SELECT m.year, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.year
ORDER BY m.year;
