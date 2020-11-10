def get_unique_genre_from_album(albums):
    genre_list = [album.genre for album in albums]
    return list(set(genre_list))
