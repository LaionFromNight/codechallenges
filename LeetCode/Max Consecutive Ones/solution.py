class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        result, count = 0, 0

        for num in nums:
            count = count + 1 if num else 0
            result = count if count > result else result

        return result