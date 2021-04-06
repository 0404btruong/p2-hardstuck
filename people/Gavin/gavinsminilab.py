class Superhero:
    def __init__(self, series):
        if series < 0 or series > 10:
            raise ValueError("Must be between 0 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.superheo_series()

    def superhero_series(self):
        limit = self._series
        f = [(random.sample((superherolist1), k=3))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1

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
    x = 7
    superherobest = superhero(x/x)
    print(f"Here are some awesome superheroes! = {superherobest.list}")

if request.method == 'POST' :
    x= int(request.form.get("series"))
    superherobest = superhero(x/x)
    return render_template("select-superhero.html", superherobest=superheroes(int(request.form.get("series"))))
return render_template("select-book.html", superherobest=superheroes(1))

