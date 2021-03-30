"""Paraphrased off of morts code for the fibonacci series"""


class FibonacciSeries:
    def __init__(self, series):
        if series < 2 or series > 100:
            raise ValueError("Must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.calculate_series()
        
    def calculate_series(self):
        limit = self._series
        f = [0, 1]  
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], f[0] + f[1]]
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
    n = 69
    fibonacci = FibonacciSeries(n)
    print(f"Fibonacci number for {n} = {fibonacci.number}")
    print(f"Fibonacci series for {n} = {fibonacci.list}")
    for i in range(n):
        print(f"Fibonacci sequence {i + 1} = {fibonacci.get_sequence(i)}")
