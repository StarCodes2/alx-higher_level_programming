-- Imports a database dump from hbtn_0d_tvshows
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id ASC;
