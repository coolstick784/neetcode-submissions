class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        left = 1
        right = mx
        def possible(m):
            cur = 0
            for p in piles:
                cur += math.ceil(p/m)
            if cur <= h:
                return True
            return False
        while left < right:
            med = (left + right) // 2
            if possible(med):
                right = med - 1
            else:
                left = med + 1
        if possible(left):
            return left
        return left + 1