__copyright__ = 'Copyright(c) Gordon Elliott 2016'

import unittest

from challenge.top_n import top_n, NumberParseError, numbers_from_strings


class TopNTest(unittest.TestCase):
    """ Functional tests for top_n()
    """

    def test_empty(self):
        self.assertListEqual([], top_n(8, []))

    def test_fewer_than_n(self):
        self.assertListEqual(
            [9, 4, 3, 2], top_n(6, [3, 4, 9, 2])
        )

    def test_exactly_n(self):
        self.assertListEqual(
            [9, 4, 3, 2], top_n(4, [3, 4, 9, 2])
        )

    def test_2_n(self):
        self.assertListEqual(
            [9, 8, 7, 5], top_n(4, [3, 4, 9, 2, 5, 3, 7, 8])
        )

    def test_in_order(self):
        self.assertListEqual(
            list(range(29, 22, -1)), top_n(7, range(30))
        )

    def test_in_reverse_order(self):
        self.assertListEqual(
            list(range(29, 22, -1)), top_n(7, reversed(range(30)))
        )

    def test_floats(self):
        list_of_floats = [
            81.30740443788693, 44.24342978727118, 28.203614965655742, 18.725865488033456, 29.86912386075753,
            62.50757716141009, 40.5264998767475, 96.88767648971032, 75.77647527812306, 26.224015693501634,
            49.268463760737966, 10.376594567714559, 21.90906815033934, 15.29329518115058, 86.91796226576156,
            32.161963482964694, 24.983728727349142, 64.36488000578608, 40.95257161221036, 12.274245609078527
        ]
        self.assertListEqual(
            [96.88767648971032, 86.91796226576156, 81.30740443788693, 75.77647527812306],
            top_n(4, list_of_floats)
        )


class NumbersFromStringsTest(unittest.TestCase):
    """ Test a sequence of numbers can be converted correctly
    """

    def test_empty_file(self):
        self.assertEqual([], list(numbers_from_strings([], int)))

    def test_bad_float(self):
        with self.assertRaises(NumberParseError):
            list(numbers_from_strings(['0.93839', '0.0not a float'], float))

    def test_bad_int(self):
        with self.assertRaises(NumberParseError):
            list(numbers_from_strings(['44', '33.5'], int))

    def test_expected_conversion(self):
        self.assertListEqual(
            [3, 9, 44],
            list(numbers_from_strings(['3', '9', '44'], int))
        )
