import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode_max_consecutive_onse(unittest.TestCase):

    @parameterized.expand([
        ([12,345,2,6,7896], 2),
        ([555,901,482,1771], 1)
    ])
    def test_csv_helper_generate_headers_for_output_multiple(self, input, expect_result):
        # Assume
        test = Solution()

        # Action
        result = test.findNumbers(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
