import unittest

from find_matching_pair import find_matching_pair


class TestFindMatchingPair(unittest.TestCase):
    def test_matching_pair_exists(self):
        arr = [2, 3, 6, 7]
        target_sum = 9

        self.assertEqual(find_matching_pair(arr, target_sum), (2, 7))

    def test_matching_pair_does_not_exist(self):
        arr = [1, 3, 3, 7]
        target_sum = 9
        self.assertEqual(find_matching_pair(arr, target_sum), None)

    def test_empty_array(self):
        arr = []
        target_sum = 5
        self.assertEqual(find_matching_pair(arr, target_sum), None)

    def test_single_element_array(self):
        arr = [5]
        target_sum = 5
        self.assertEqual(find_matching_pair(arr, target_sum), None)

    def test_negative_numbers(self):
        arr = [-2, 3, 5, 8]
        target_sum = 1
        self.assertEqual(find_matching_pair(arr, target_sum), (-2, 3))


if __name__ == "__main__":
    unittest.main()
