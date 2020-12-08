class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums[:] = [num for num in nums if num != val]

        return len(nums)