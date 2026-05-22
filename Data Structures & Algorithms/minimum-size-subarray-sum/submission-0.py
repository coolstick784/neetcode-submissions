class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0 
        right = 0
        cur = 0
        while right < len(nums):
            cur += nums[right]
            while cur >= target:
                res = min(res, right-left + 1)

                cur -= nums[left]
                left += 1


            right += 1
        if res == float('inf'):
            return 0
        return res