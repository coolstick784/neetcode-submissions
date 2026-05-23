# have a current
# if end < newInterval[start], append [start, end] to res
# if end >=start, cur = [start, newEnd]
# then continue

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        cur = newInterval.copy()
        res = []
        if not intervals:
            return [newInterval]

        for start, end in intervals:
            
            if not cur:
                res.append([start, end])
                continue
            curStart, curEnd = cur
            if (curStart >= start and curStart <= end) or (curEnd >= start and curEnd <= end) or (curStart <= start and curEnd >= end):
                cur = [min(curStart, start), max(curEnd, end)]
            elif start > curEnd:
                res.append(cur)
                res.append([start, end])
                cur = []
            else:
                res.append([start, end])
        if cur:
            res.append(cur)

        return res