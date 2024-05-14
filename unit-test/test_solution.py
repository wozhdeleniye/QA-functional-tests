import unittest
from solutions.unit_solution import Solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()
    def test_task_example1(self):
        self.assertEqual(self.sut.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
    def test_task_example2(self):
        self.assertEqual(self.sut.eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
    def test_task_example3(self):
        self.assertEqual(self.sut.eraseOverlapIntervals([[1,2],[2,3]]), 0)
    def test_array_length_in_range(self):
        data = {
            1: [[1, 2]],
            2: [[1, 2], [1, 2]],
            104: [[1, 2]] * 104,
            105: [[1, 2]] * 105
        }
        for k, v in data.items():
            with self.subTest(k):
                self.assertEqual(self.sut.eraseOverlapIntervals(v), k-1)
    def test_array_length_out_of_range(self):
        data = {
            0: [],
            106: [[1, 2]] * 106
        }
        for k, v in data.items():
            with self.assertRaises(ValueError):
                self.sut.eraseOverlapIntervals(v)
    def test_inner_array_length_in_range(self):
        data = {
            2: [[1, 2]]
        }
        for k, v in data.items():
            with self.subTest(k):
                self.assertEqual(self.sut.eraseOverlapIntervals(v), 0)
    def test_inner_array_length_out_of_range(self):
        data = {
            1: [[1]],
            3: [[1, 2, 3]]
        }
        for k, v in data.items():
            with self.assertRaises(ValueError):
                self.sut.eraseOverlapIntervals(v)
    def test_value_in_range(self):
        data = {
            2: [[-5 * 104, 5 * 104]]
        }
        for k, v in data.items():
            with self.subTest(k):
                self.assertEqual(self.sut.eraseOverlapIntervals(v), 0)

    def test_value_out_of_range(self):
        data = {
            "out of range": [[-5 * 104 - 1, 5 * 104 + 1]],
            "second smaller": [[5 * 104 + 1, -5 * 104 - 1]]
        }
        for k, v in data.items():
            with self.assertRaises(ValueError):
                self.sut.eraseOverlapIntervals(v)
    def test_value_is_not_integer(self):
        data = {
            "русский": [["абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"]],
            "english": [["qwertyuiopasdfghjklzxcvbnm", "qwertyuiopasdfghjklzxcvbnm"]]
        }
        for k, v in data.items():
            with self.assertRaises(ValueError):
                self.sut.eraseOverlapIntervals(v)