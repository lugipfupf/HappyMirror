import unittest

from .quote import Renderer


class TestQuote(unittest.TestCase):
    def setUp(self) -> None:
        self.quote = Renderer()


    def test_next(self):
        self.assertIsNotNone(self.quote.next())


if __name__ == '__main__':
    unittest.main()
