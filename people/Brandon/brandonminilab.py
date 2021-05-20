class RandomAlgebra:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 100 :
            raise ValueError("Series must be between 0 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.random_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building random algebra, this id called from __init__"""
    def random_series(self):
        limit = self._series
        f = [0]  # random starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[2] * f[1] + f[10] / f[3]]
            limit -= 1

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 1
    '''Constructor of Class object'''
    random = RandomAlgebra(n)

    '''Using getters to obtain data from object'''
    print(f"random number for {n} = {random.number}")
    print(f"random series for {n} = {random.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"random sequence {i + 1} = {random.get_sequence(i)}")
