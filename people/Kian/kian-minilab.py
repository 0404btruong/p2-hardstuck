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
        cap = self._series
        f = [0, 1]  
        while cap > 0:
            self.set_data(f[0])
            f = [f[1], f[0] + f[1]]
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
    n = 69
    fibonaccifinal = FibonacciSeries(n)
    print(f"Fibonacci number for {n} = {fibonaccifinal.value}")
    print(f"Fibonacci series for {n} = {fibonaccifinal.list}")
    for i in range(n):
        print(f"Fibonacci sequence {i + 1} = {fibonaccifinal.get_sequence(i)}")
