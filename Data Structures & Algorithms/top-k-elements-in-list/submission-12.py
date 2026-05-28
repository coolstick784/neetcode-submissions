class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        rev = {}
        for n, c in ctr.items():
            rev.setdefault(c, []).append(n)
        cur = len(nums)
        res = []
        while len(res) < k:
            res.extend(rev.get(cur, []))
            cur -= 1
        return res