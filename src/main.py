import fibo 
import unittest as ut

class Test(ut.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibo.fibonacci(5), 3)

if __name__ == '__main__':
    ut.main()