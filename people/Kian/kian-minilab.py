"""Paraphrased off of morts code for the fibonacci series"""
import random

movieseries = ['Star Trek', 'Star Wars', 'Avengers', 'DC', 'Saw', 'Now You See Me', 'Jumanji']
movies = ['Parasite', 'Joker', 'Insideous', 'Inception', 'Godzilla: King of Monsters', 'Suicide Squad', 'Interstellar', 'Upgrade', 'Vivarium', 'Gravity', 'Napoleon Dynamite']

class Movies:
    def __init__(self, series):
        if series < 0 or series > 11:
            raise ValueError("Must be between 0 and 11")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.movie_series()
        
    def movie_series(self):
        cap = self._series
        f = [random.sample((movies), k=int(input("How many movies do you want? (Up to 11)")))]
        while cap > 0:
            self.set_data(f[0])
            f = [f[0]]
            cap -= 1

    def set_data(self, numbers):
        self._list.append(numbers)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def value(self):
        return self._list[self._dictID - 1]
        
    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    a = int(input("Pick a number from 0 and 11"))
    movies = Movies(a)
    print(f"Movie recommendations: = {movies.list}")
