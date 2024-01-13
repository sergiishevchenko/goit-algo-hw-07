import unittest

from avl import AVLNode
from generate_random_numbers import generate_random_numbers


class AVLNodeTest(unittest.TestCase):
    def setUp(self):
        self.tree = AVLNode()
        self.root = None

    def test_get_max_value(self):
        for i in range(1, 100):
            random_numbers = generate_random_numbers(50)
            max_num = max(random_numbers)

            for random_number in random_numbers:
                self.root = self.tree.insert(self.root, random_number)

            self.assertEqual(max_num, self.tree.get_max_value(self.root))

    def test_get_min_value(self):
        for i in range(1, 100):
            random_numbers = generate_random_numbers(50)
            min_num = min(random_numbers)

            for random_number in random_numbers:
                self.root = self.tree.insert(self.root, random_number)

            self.assertEqual(min_num, self.tree.get_min_value(self.root))

    def test_calculate(self):
        for i in range(1, 100):
            random_numbers = generate_random_numbers(50)
            summ = sum(random_numbers)

            for random_number in random_numbers:
                self.root = self.tree.insert(self.root, random_number)

            self.assertEqual(summ, self.tree.calculate(self.root))


if __name__ == '__main__':
    unittest.main()