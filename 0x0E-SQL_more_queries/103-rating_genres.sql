-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) AS rating
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
LEFT JOIN tv_show_ratings AS tsr
ON ts.id = tsr.show_id
GROUP BY tg.name;
