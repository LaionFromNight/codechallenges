import unittest
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([10,2,5,3], True),
        ([7,1,14,11], True),
        ([3,1,7,11], False)
    ])
    def test_multiple(self, input, expect_result):
        # Assume
        test = Solution()

        # Action
        result = test.checkIfExist(input)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
