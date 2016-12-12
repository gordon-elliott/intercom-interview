__copyright__ = 'Copyright(c) Gordon Elliott 2016'

""" Problem

Write a program, topN, that given an arbitrarily large file and a number, N, containing
individual numbers on each line (e.g. 200Gb file), will output the largest N numbers,
highest first. Tell me about the run time/space complexity of it, and whether you think
there's room for improvement in your approach.

"""

import argparse
import sys

from itertools import islice


FROM_STRING = {
    "int": int,
    "float": float
}


def top_n(n, to_search):
    """ List the top N numbers in an iterable of numbers

    :param n: int how many numbers to return
    :param to_search: iterable of numbers to search through
    :return: list of n numbers
    """
    # ensure to_search is an iterator
    to_search = iter(to_search)

    # initialise the list of top numbers with the first n numbers in the list
    top_numbers = list(
        sorted(
            islice(to_search, n),
            reverse=True
        )
    )

    # compare the remaining numbers with the smallest of the top numbers
    for number in to_search:
        least_of_top_n = top_numbers[-1]
        if number > least_of_top_n:
            # replace the least if the current number is greater than it
            top_numbers[-1] = number

            top_numbers = sorted(top_numbers, reverse=True)

    return top_numbers


class NumberParseError(Exception):
    pass


def numbers_from_strings(number_strings, as_number):
    """ Cast strings to numbers

    :param number_strings: iterable of strings
    :param as_number: function to cast string to int or float
    :return: generator for numbers
    """
    line_no = 0
    line = ''
    try:
        for line_no, line in enumerate(number_strings):
            number = as_number(line)
            yield number
    except ValueError:
        raise NumberParseError("Error in line {}, {}".format(line_no, line))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("type", default="int", choices=("int", "float"))
    parser.add_argument('number_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()

    try:
        as_number = FROM_STRING[args.type]
        print(
            '\n'.join(map(str,
                top_n(
                    args.n,
                    numbers_from_strings(args.number_file, as_number)
                )
            ))
        )
    finally:
        if not args.number_file.closed:
            args.number_file.close()
