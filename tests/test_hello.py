import charming as app
import unittest


class HelloTest(unittest.TestCase):
    def setUp(self):
        print('test begin')

    def test_hello(self):
        self.assertEqual(app.hello(), 'hello world')

    def tearDown(self):
        print('test end')


class OtherTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
