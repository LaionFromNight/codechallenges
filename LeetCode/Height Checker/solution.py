class Solution:
    def heightChecker(self, heights) -> int:
        _sorted = sorted(heights)
        return sum(heights[i] != _sorted[i] for i in range(len(heights)))