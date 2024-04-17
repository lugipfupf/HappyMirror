import unittest

from .hello import Renderer

class TestQuote(unittest.TestCase):
    def setUp(self) -> None:
        self.renderer = Renderer()


    def test_render(self) -> None:
        result = self.renderer.render()
        self.assertIn('view', result)


if __name__ == '__main__':
    unittest.main()
