-- 11-genre_id_all_shows.sql
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows a
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
