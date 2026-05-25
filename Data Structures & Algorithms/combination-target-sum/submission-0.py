from functools import lru_cache
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(list(set(nums)))
        @lru_cache(None)
        def solve(n, start):
            if n == 0:

                return [[]]
            out = []
            for idx in range(start, len(nums)):
                num = nums[idx]
                if n < num:
                    continue
                cur = [num]
                for arr in solve(n-num, idx):

                    out.append(cur + arr)
  
            return out
        
        return solve(target, 0)