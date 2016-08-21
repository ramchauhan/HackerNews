class FibCalculator(object):
    """
    class which is used to calculate the fib and timeit
    """
    def __init__(self, num):
        self.num = num

    def get_nth_number(self):
        """
        this will give the nth number of the Fibonacci series which will start from [1, 1, ....]
        :return:
            Nth number of the fibonacci series
        """
        return list(self._fib_series_gen())[self.num - 1]

    def _fib_series_gen(self):
        """
        this will give the nth number of the Fibonacci series which will start from [1, 1, ....]
        :return:
            Nth number of the fibonacci series
        """
        a, b = 1, 1
        for _ in range(self.num + 1):
            yield a
            a, b = b, a + b
