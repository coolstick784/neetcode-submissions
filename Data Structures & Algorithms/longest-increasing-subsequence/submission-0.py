from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        explored = set()
        @lru_cache(None)
        def longest(start):
            res = 1
            
            for idx2 in range(start+1, len(nums)):
                n = nums[idx2]
                if n > nums[start]:
                    res = max(res, 1 + longest(idx2))
            explored.add(start)
            return res

        long = 1
        for idx, n in enumerate(nums):
            if idx not in explored:
                long = max(long, longest(idx))
        return long