class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            left = heights[l]
            right = heights[r]
            if left < right:
                res = max(res, left * (r-l))
                l += 1
            else:
                res = max(res, right * (r-l))
                r -= 1

        return res