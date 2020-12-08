import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        test = Solution()

        # Action
        result = test.thirdMax(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
