select title, genre_id from tv_shows Full join tv_show_genres on id = tv_show_genres.show_id order by title, tv_show_genres.genre_id ;