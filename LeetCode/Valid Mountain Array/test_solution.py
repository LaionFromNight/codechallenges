import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([2,1], False),
        ([3,5,5], False),
        ([0,3,2,1], True),
        ([0,2,3,4,5,2,1,0], True),
        ([0,2,3,3,5,2,1,0], False),
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        test = Solution()

        # Action
        result = test.validMountainArray(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
