import requests

class Song:
    def __init__(self, song_id, header):
        self._song_id = song_id

        # dummy variables will be in place until api can be accessed for actual values related to songs from api
        # artist, album, genre, length, listeners, release_date = 1, 1, 1, 1, 1, 1

        # dummy access to spotify
        spotify_song = requests.get("https://api.spotify.com/", headers=header.add({'id': song_id})).json().get()
        spotify_song_audio = requests.get("https://api.spotify.com/", headers=header.add({'id': song_id})).json().get()

        song_name = spotify_song["album"]["tracks"]["name"]
        artist = spotify_song["album"]["artists"]["name"]
        album = spotify_song["album"]["name"]
        genre = 'filler'
        length = spotify_song_audio["duration_ms"]
        listeners = 'filler'
        release_date = spotify_song["album"]["release_date"]
        # note: 'filler' denotes finding api access for that specific thing later

        self._song_name = song_name
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
        if int(self._listeners) >= 10000:
            score += 0.05 * int(self._listeners)

        return score

    def similar(self, total_list, id_list):
        return [k for k in total_list[self._genre] if
                Song(k, id_list[k]).genre == Song(self._song_name, id_list[k])]  # add other conditions in this line

    @property
    def id(self):
        return self._song_id

    @property
    def song_name(self):
        return self._song_name

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


if __name__ == "__main__":
    header = {
        'Authorization': 'insert key here'
    }
    spotify = requests.get("https://api.spotify.com/", headers=header)
    song_id = 'insert id'
    Spotify = Song(song_id, header)
    print(f"{Spotify.song_name} has the id of {Spotify.id}")
    print(f"It was created by {Spotify.artist} in the album {Spotify.album}")