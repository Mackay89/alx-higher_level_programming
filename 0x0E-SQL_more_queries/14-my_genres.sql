-- task: Script to list all genres of the show Dexter from hbtn_0d_tvshows database
-- Uses a database to lists all row in a table corresponding to all rows in another
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
