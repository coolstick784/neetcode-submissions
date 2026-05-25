class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        # if cur >= 1 + next, remove next
        cur = 0
        new = 0
        for idx, n in enumerate(nums[:-1]):
            if cur == 0:
                cur = max(new-1, n)
                res += 1
            else:
                new = max(new-1, n)
            cur -= 1
        return res
            