import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

    def test_zero(self):
        self.assertEqual(fun(0), 1)

    def test_negative(self):
        self.assertEqual(fun(-5), -4)
if __name__ == '__main__':
    unittest.main()