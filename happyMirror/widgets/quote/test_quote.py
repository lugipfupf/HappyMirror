import unittest
import requests_mock

from .quote import Renderer
from . import quote_config_example


class TestQuote(unittest.TestCase):
    def setUp(self) -> None:
        self.API_BASE_URL = 'https://api.api-ninjas.com/v1/quotes'
        self.TEST_RESULT = '[{"quote": "Tis but a scratch", "author": "Black Knight"}]'
        self.TEST_API_KEY = '0000000000000000000000000000000000000000'


    @requests_mock.Mocker()
    def test_next(self, m):
        m.get(
            self.API_BASE_URL + '?category=monty-python',
            text=self.TEST_RESULT
        )

        config = quote_config_example
        config.api_key = self.TEST_API_KEY
        quote = Renderer(alt_config=config)
        result = quote.next('monty-python')

        self.__assert_result(result)

    @requests_mock.Mocker()
    def test_next_with_no_category(self, m):
        m.get(
            self.API_BASE_URL,
            text=self.TEST_RESULT
        )

        config = quote_config_example
        config.api_key = self.TEST_API_KEY
        quote = Renderer(alt_config=config)

        result = quote.next()

        self.__assert_result(result)


    @requests_mock.Mocker()
    def test_next_with_no_apikey(self, m):
        m.get(
            self.API_BASE_URL,
            text=self.TEST_RESULT
        )

        config = quote_config_example
        config.api_key = '1234'
        quote = Renderer(alt_config=quote_config_example)

        result = quote.next()

        self.assertEqual(result[0]['quote'], 'NO API KEY SET IN CONFIG FILE')
        self.assertEqual(result[0]['author'], "'Quote' widget")

    def __assert_result(self, result):
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['quote'], 'Tis but a scratch')
        self.assertEqual(result[0]['author'], 'Black Knight')


if __name__ == '__main__':
    unittest.main()
