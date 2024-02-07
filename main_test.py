import unittest
from main import get_thousand

# TODO: For now we have tests only for one function. It is the main one since it is this function that we call
# to obtain the text value for a given number.
# But ideally other functions should have tests as well.


class TestGetThousand(unittest.TestCase):

    def test_get_thousand_10000(self):
        self.assertEqual(get_thousand(10000, from_france=False), "dix-milles")

    def test_get_thousand_10000_from_france(self):
        self.assertEqual(get_thousand(10000, from_france=True), "dix-milles")

    def test_get_thousand_999999(self):
        self.assertEqual(
            get_thousand(999999, from_france=False),
            "neuf-cent-nonante-neuf-mille-neuf-cent-nonante-neuf",
        )

    def test_get_thousand_999999_from_france(self):
        self.assertEqual(
            get_thousand(999999, from_france=True),
            "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf",
        )

    def test_get_thousand_100(self):
        self.assertEqual(get_thousand(100, from_france=False), "cent")

    def test_get_thousand_100_from_france(self):
        self.assertEqual(get_thousand(100, from_france=True), "cent")
