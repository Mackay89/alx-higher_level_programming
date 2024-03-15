-- task: Script to list all genres not linked to the show Dexter from the hbtn_0d_tvshows database
-- lists all rows of a table linked to another table
SELECT name
FROM tv_genres
WHERE name NOT IN (SELECT name FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genres_id LEFT JOIN  tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
