from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ctr = Counter(nums)
        total = len(nums)
        goal = total - k + 1
        cur = 0
        for n in range(-1000, 1001):
            cur += ctr.get(n, 0)
            if cur >= goal:
                return n