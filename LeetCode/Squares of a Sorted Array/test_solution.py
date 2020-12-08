import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([-7,-3,2,3,11], [4,9,9,49,121]),
        ([-4,-1,0,3,10], [0,1,9,16,100])
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        test = Solution()

        # Action
        result = test.sortedSquares(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
