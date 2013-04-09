
import unittest


def throw_value_error():
    int('asdfasdf')


class NotReallyATest(unittest.TestCase):
    def test_example(self):
        self.assertRaises(Exception, throw_value_error)
