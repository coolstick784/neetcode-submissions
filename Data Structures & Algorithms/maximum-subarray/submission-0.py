class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = max(nums)
        for n in nums:
            cur += n
            cur = max(cur, 0)
            if cur > 0:
                best = max(best, cur)
        return best