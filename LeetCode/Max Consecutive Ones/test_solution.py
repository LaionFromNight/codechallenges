import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([1, 1, 0, 1, 1, 1], 3),
        ([1,0,1,1,0,1], 2)
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        test = Solution()

        # Action
        result = test.findMaxConsecutiveOnes(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
