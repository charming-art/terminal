import charming as app
import unittest
import math


class ConstantsTest(unittest.TestCase):

    def test_constents(self):
        self.assertEqual(app.PI, math.pi)
        self.assertEqual(app.HALF_PI, math.pi / 2)
        self.assertEqual(app.QUARTER_PI, math.pi / 4)
        self.assertEqual(app.TWO_PI, math.pi * 2)
        self.assertEqual(app.TAU, math.pi * 2)


if __name__ == "__main__":
    unittest.main()
