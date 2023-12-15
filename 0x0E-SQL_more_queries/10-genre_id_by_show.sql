-- Imports a database dump from hbtn_0d_tvshows
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.genre_id
ORDER BY ts.title, tg.genre_id ASC;
