class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        rev = {}
        max_c = 0
        for n, c in ctr.items():
            rev.setdefault(c, []).append(n)
            max_c = max(max_c, c)
        cur = max_c
        res = []
        while len(res) < k:
            res.extend(rev.get(cur, []))
            cur -= 1
        return res