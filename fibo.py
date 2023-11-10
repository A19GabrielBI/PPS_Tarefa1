import unittest as ut

def fibonacci(pos: int) -> int:
    first = 0
    second = 1
    posCounter = 1
    while posCounter < pos:
        second += first
        first = second - first
        posCounter += 1
    return first

class Test(ut.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 3)

if __name__ == '__main__':
    ut.main()