import unittest
from collections import Counter
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([1,1,2],
         2, [1,2]
         ),
        ([0,0,1,1,1,2,2,3,3,4],
         5, [0,1,2,3,4]
        )
    ])
    def test_multiple(self, input, expect_result, expected_input):
        # Assume
        test = Solution()
        original_input = input.copy()

        # Action
        result = test.removeDuplicates(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(original_input, expect_result, result))

        self.assertEqual(input, expected_input,
                         "The result for input {} should be {} but is {}".format(original_input, expected_input, input))
