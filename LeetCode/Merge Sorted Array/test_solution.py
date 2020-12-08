import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        (
            [1, 2, 3, 0, 0, 0], 3,
            [2,5,6], 3,
            [1, 2, 2, 3, 5, 6]
        ),
        (
            [1, 2, 3, 0, 0, 0], 4,
            [1, 1], 2,
            [0, 1, 1, 1, 2, 3]
        ),
        (
            [1, 2, 3, 4, 5, 6], 4,
            [15, 16], 2,
            [1, 2, 3, 4, 15, 16]
        ),
    ])
    def test_multiple(self, num1, m, num2, n, expect_result):
        # Assume
        test = Solution()
        original_input = num1.copy()

        # Action
        test.merge(num1, m , num2, n)

        # Asert
        self.assertEqual(num1, expect_result,
                         "The result for input {} should be {} but is {}".format(original_input, expect_result, num1))
