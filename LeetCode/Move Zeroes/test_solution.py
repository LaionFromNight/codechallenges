import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([0,1,0,3,12], [1,3,12,0,0]),
        ([0,21,0,8,0], [21,8,0,0,0])
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        original_input = input.copy()
        test = Solution()

        # Action
        test.moveZeroes(input)

        # Asert
        self.assertEqual(input, expect_result,
                         "The result for input {} should be {} but is {}".format(original_input, expect_result, input))
