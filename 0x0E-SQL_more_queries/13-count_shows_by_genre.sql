-- task: Script to list all genre from hbtn_0d_tvshows database and display the number of shows linked to each
--lists all rows of database meeting a condition
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY number_of_shows DESC;
