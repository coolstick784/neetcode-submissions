# for each number, find edges
# expand as high and low as you possibly can, removing those along the way, 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best = 1
        set_nums = set(nums)
        for n in nums:
            if n not in set_nums:
                continue
            set_nums.remove(n)
            cur = 1
            cur_n = n
            while cur_n + 1 in set_nums:
                cur_n += 1
                cur += 1
                set_nums.remove(cur_n)
            cur_n = n
            while cur_n - 1 in set_nums:
                cur_n -= 1
                cur += 1
                set_nums.remove(cur_n)
            best = max(best, cur)
        return best



