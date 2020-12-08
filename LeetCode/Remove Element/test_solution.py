import unittest
from collections import Counter
from parameterized import parameterized
from solution import Solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ([3,2,2,3], 3,
         2, [2,2]
         ),
        ([0,1,2,2,3,0,4,2], 2,
         5, [0,1,4,0,3]
        )
    ])
    def test_multiple(self, input, val, expect_result, expected_input):
        # Assume
        test = Solution()
        original_input = input.copy()

        # Action
        result = test.removeElement(input, val)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(original_input, expect_result, result))

        """
        Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. 
        Note that the order of those five elements can be arbitrary. 
        It doesn't matter what values are set beyond the returned length.
        
        To mach to arry not sorted we can use Counter or sort them
        """
        self.assertEqual(Counter(input), Counter(expected_input),
                         "The result for input {} should be {} but is {}".format(original_input, expected_input, input))
