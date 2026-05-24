class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in nums]
        for idx, n in enumerate(nums):

            cur = n
            if idx >= 2:
                cur = dp[idx-2] + n
            if idx >= 3:
                cur = max(cur, dp[idx-3] + n)
            dp[idx] = cur 
            

        return max(dp[-1], dp[-2])