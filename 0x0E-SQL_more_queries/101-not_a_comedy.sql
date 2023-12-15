-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT ts.title
FROM tv_genres AS tg
RIGHT JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
RIGHT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE ts.title NOT IN
	(SELECT title
	 FROM tv_genres AS tg
		INNER JOIN tv_show_genres AS tsg
		ON tg.id = tsg.genre_id
		INNER JOIN tv_shows AS ts
		ON tsg.show_id = ts.id
	 WHERE tg.name = "Comedy")
ORDER BY ts.title ASC;
