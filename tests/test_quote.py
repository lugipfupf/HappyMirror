import unittest

from happyMirror.quote import Quote

class TestQuote(unittest.TestCase):
    def setUp(self) -> None:
        self.quote = Quote()


    def test_next(self):
        self.assertEqual(self.quote.next(), "Heute wird ein guter Tag!")

if __name__ == '__main__':
    unittest.main()
