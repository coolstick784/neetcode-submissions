class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_val = float('inf')
        nums = [0] + nums
        i = 0
        while i < len(nums):
            n = nums[i]
            if n <= 0 or n >= len(nums):

                i += 1
            elif i == n:
                i += 1
            elif nums[n] != n:
                nums[i], nums[n] = nums[n], nums[i]
            else:
                i += 1
        
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            if n != idx:
                return idx
        return len(nums)