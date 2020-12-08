import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([1,0,2,3,0,4,5,0], [1,0,0,2,3,0,0,4]),
        ([1,2,3], [1,2,3]),
        ([0,0,1,2,3], [0,0,0,0,1])
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        original_input = input.copy()
        test = Solution()

        # Action
        test.duplicateZeros(input)

        # Asert
        self.assertEqual(input, expect_result,
                         "The result for input {} should be {} but is {}".format(original_input, expect_result, input))
