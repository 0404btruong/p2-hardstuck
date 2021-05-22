class Song:
    def __init__(self, name, song_id):
        self._name = name
        self._id = song_id

        # dummy variables will be in place until api can be accessed for actual values related to songs from api
        artist, album, genre, length, listeners, release_date = 1, 1, 1, 1, 1, 1
        self._artist = artist
        self._album = album
        self._genre = genre
        self._length = length
        self._listeners = listeners
        self._release_date = release_date

    def song_score(self, genre_preferences, artist_preferences, recent_played_albums):
        score = 0

        # dummy multipliers will be added and fine tuned once there is content to actually analyze
        score += (12 - 2 * [k for k in range(len(genre_preferences)) if genre_preferences[k] == self._genre][0])
        if self._artist in artist_preferences:
            score += 6
        if self._album in recent_played_albums:
            score += 4
        if self._listeners >= 10000:
            score += 0.05 * int(self._listeners)

        return score

    def similar(self, total_list, id_list):
        return [k for k in total_list[self._genre] if
                Song(k, id_list[k]).genre == Song(self._name, id_list[k])]  # add other conditions in this line

    @property
    def artist(self):
        return self._artist

    @property
    def album(self):
        return self._album

    @property
    def genre(self):
        return self._genre

    @property
    def length(self):
        return self._length

    @property
    def listeners(self):
        return self._listeners

    @property
    def release_date(self):
        return self._release_date


class User:
    def __init__(self):
        self._favorites = []
