-- task: Script to list all genres not linked to the show Dexter from the hbtn_0d_tvshows database
-- lists all rows of a table linked to another table
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title != 'Dexter' or tv_shows.title IS NULL
ORDER BY title ASC, name ASC;
