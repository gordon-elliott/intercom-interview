__copyright__ = 'Copyright(c) Gordon Elliott 2016'

""" Performance profiling for top_n()
"""
import random

from time import time
from functools import partial

from challenge.top_n import top_n


def timer(fn, iterations):
    """ Compute the time taken to run a function a number of times

    :param fn: function to time
    :param iterations: int number of iterations
    :return: float total time to execute the function
    """
    start = time()
    for _ in range(iterations):
        fn()
    duration = time() - start
    return duration


def test_performance():
    """ Establish how performance of top_n() varies with the length of the list it is processing
    """

    timing_iterations = 10000
    orders_of_magnitude = 8

    for power_of_ten in range(orders_of_magnitude):
        list_length = 10 ** power_of_ten

        # create a callable which invokes top_n() for a defined list length
        random_ints = (random.randint(0, list_length * 2) for _ in range(list_length))
        top_10 = partial(top_n, 10, random_ints)

        # time the function
        duration = timer(top_10, timing_iterations)

        print(
            "list length: {:>8}, time per list item: {:.12f} secs".format(
                list_length,
                duration / list_length
            )
        )


if __name__ == "__main__":
    test_performance()

"""
Sample results

list length:        1, time per list item: 0.035306930542 secs
list length:       10, time per list item: 0.001372361183 secs
list length:      100, time per list item: 0.000140628815 secs
list length:     1000, time per list item: 0.000039357424 secs
list length:    10000, time per list item: 0.000006821585 secs
list length:   100000, time per list item: 0.000001685996 secs
list length:  1000000, time per list item: 0.000001519433 secs
list length: 10000000, time per list item: 0.000001529219 secs


The results above illustrate that the algorithm operates in O(n) time. That is
the time the function takes will grow at the same rate as the number of items
in the list it is searching.

Once the program is processing lists of 100,000 elements or more the start up time
becomes negligible and the time per item converges around 0.0000015 seconds.

The space taken by the program is proportional to the number of results it will
return i.e. the parameter 'n'. This can be clearly seen as there is just one
data structure created:

    top_numbers = list(...

This list never exceeds 'n' elements in length.

The next target for performance improvements would be reading the input file. There
are fairly conventional techniques for dealing with this but they are filesystem
dependent. Using BufferedReader in order that entire blocks are read from disk at
a time would probably be worth exploring.

If it is desired to scale out the solution to run on multiple processors it is worth noting
that top_n() can be used as the reduce step in a map-reduce division of the processing.

"""