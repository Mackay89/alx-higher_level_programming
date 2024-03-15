-- task: Script to list all shows and their linked genres from the hbtn_0d_tvshows database
-- lists all rows of a database corresponding to a column value
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC
