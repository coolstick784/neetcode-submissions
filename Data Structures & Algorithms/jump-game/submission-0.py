class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_len = 1
        cur_idx = 0
        while cur_idx < len(nums) and cur_len > 0:
            cur_len -= 1
            cur_len = max(cur_len, nums[cur_idx])
            cur_idx += 1
            
        if cur_idx < len(nums):
            return False
        return True