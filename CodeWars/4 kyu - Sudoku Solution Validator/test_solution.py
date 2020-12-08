import unittest
from parameterized import parameterized
import solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 5, 3, 4, 8],
           [1, 9, 8, 3, 4, 2, 5, 6, 7],
           [8, 5, 9, 7, 6, 1, 4, 2, 3],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 6, 1, 5, 3, 7, 2, 8, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 4, 5, 2, 8, 6, 1, 7, 9]], True),
        ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 0, 3, 4, 9],
           [1, 0, 0, 3, 4, 2, 5, 6, 0],
           [8, 5, 9, 7, 6, 1, 0, 2, 0],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 0, 1, 5, 3, 7, 2, 1, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 0, 0, 4, 8, 1, 1, 7, 9]], False),
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        original_input = input.copy()

        # Action
        result = solution.validSolution(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
