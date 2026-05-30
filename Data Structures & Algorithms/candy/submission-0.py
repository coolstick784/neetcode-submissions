class Solution:
    def candy(self, ratings: List[int]) -> int:
        lt = {}
        gt = {}
        if len(ratings) == 1:
            return 1
        for idx, r in enumerate(ratings):
            if idx == 0:
                continue
            if r > ratings[idx-1]:
                gt.setdefault(idx, set()).add(idx-1)
                lt.setdefault(idx-1, set()).add(idx)
            elif r < ratings[idx-1]:
                gt.setdefault(idx-1, set()).add(idx)
                lt.setdefault(idx, set()).add(idx-1) 
        q = deque()
        for idx, r in enumerate(ratings):
            if idx not in gt:
                q.append((idx, 1))
        res = 0
        while q:
            
            idx, candy = q.popleft()
            res += candy
            for new in lt.get(idx, set()):
                if gt.get(new, set()):
                    gt[new].remove(idx)
                    if not gt[new]:
                        del gt[new]
                        q.append((new, candy+1))
                
        
        return res