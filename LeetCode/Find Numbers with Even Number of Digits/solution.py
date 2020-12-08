class Solution:
    _len = lambda self, num: len(str(num))

    def findNumbers(self, nums) -> int:
        return len([num for num in nums if not self._len(num) % 2])