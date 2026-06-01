# if > the previous, prev  =1
# if < the previous, it'll be at most prev-1
# if it's < the prev, it can only be seen by the person right behind them
# a person can see the next one, and if it's greater than the next one, it can see the next person's end, and so on
from functools import lru_cache
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        q = deque(heights)
        dp = [0 for _ in heights]
        idx = 0


        @lru_cache(None)
        def solve(idx):
            h = heights[idx]
            if idx == len(heights) - 1:
                return len(heights)
            end = idx + 1
            dp[idx] += 1
            while end < len(heights) and h > heights[end]:
                end = solve(end)
                dp[idx] += 1
            if end == len(heights):
                dp[idx] -= 1
            return end
            
        while idx < len(heights):
            idx = solve(idx)
        return dp
        