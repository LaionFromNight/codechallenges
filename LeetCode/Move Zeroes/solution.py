class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, count = 0, 0

        while count < len(nums):
            if not nums[index]:
                del nums[index]
                nums.append(0)
            else:
                index += 1
            count += 1