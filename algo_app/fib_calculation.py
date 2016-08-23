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
        return self._fib_series_gen()

    def _fib_series_gen(self):
        """
        this will generate the nth and nth - 1 elements of fib sequence and return the nth elements of fibonacci series
        :return:
            Nth number of the fibonacci series
        """
        a, b = 1, 1
        for _ in xrange(self.num - 1):
            # updating the nth and nth - 1 elements of the Fibonacci sequence
            a, b = b, a + b
        # returning nth element
        return a