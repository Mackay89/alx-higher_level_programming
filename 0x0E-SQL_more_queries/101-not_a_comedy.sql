-- task: Script to list all shows without the genre Comedy from the the hbtn_0d_tvshows database 
-- uses a database to list all  rows not linked to one row 
SELECT title FROM tv_shows WHERE title NOT IN (SELECT title FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_show_genres.genre_id = tv_genre.id WHERE tv_genres.name = 'Comedy') GROUP BT title ORDER BY title ASC;
