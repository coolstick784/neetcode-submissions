class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in nums]
        for idx, n in enumerate(nums):
            if idx == 0:
                continue

            cur = n
            if idx >= 2:
                cur = max(cur, dp[idx-2] + n)
            if idx >= 3:
                cur = max(cur, dp[idx-3] + n)
            dp[idx] = cur 
        dp2 = [0 for _ in nums]
        for idx, n in enumerate(nums):


            cur = n
            if idx >= 2:
                cur = max(cur, dp2[idx-2] + n)
            if idx >= 3:
                cur = max(cur, dp2[idx-3] + n)
            dp2[idx] = cur 
        dp2.pop()

        return max(max(dp), max(dp2))