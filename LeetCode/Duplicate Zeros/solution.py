class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if not arr[i]:
                arr.insert(i, 0)
                arr.pop(-1)
                i += 1
            i += 1
