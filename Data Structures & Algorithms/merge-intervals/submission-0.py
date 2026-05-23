class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = []
        res = []
        for start, end in intervals:
            if not cur:
                cur = [start, end]
            elif start > cur[1]:
                res.append(cur)
                cur = [start, end]
            else:
                cur = [min(cur[0], start), max(cur[1], end)]
        res.append(cur)
        return res