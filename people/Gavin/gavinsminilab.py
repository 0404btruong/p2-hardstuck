from random import random

from flask import render_template
superherolist1= ["Superman", "Batman", "Ironman"]
class Superhero:
    def __init__(self, number):
        if number < 0 or number > 3:
            raise ValueError("Must be between 0 and 3")
        self._number = number
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.superhero_series()

    def superhero_series(self):

        f = [(random((superherolist1), k=self._number))]

        self.set_data(f[0])
        f = [f[0]]


    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    x = 2
    superherobest = Superhero(x)
    print(f"Here are some awesome superheroes! = {superherobest.list}")



