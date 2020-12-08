class Solution:
    def thirdMax(self, nums) -> int:
        _sorted = sorted(nums)

        if len(_sorted) <= 2:
            return max(_sorted)

        result, count = 0, 0
        for i in range(len(_sorted) - 1, -1, -1):
            if count == 3:
                break

            result = _sorted[i]
            if _sorted[i] != _sorted[i - 1]:
                count += 1

        if count != 3:
            return max(_sorted)
        return result
