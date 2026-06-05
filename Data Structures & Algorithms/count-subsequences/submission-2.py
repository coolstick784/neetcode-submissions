class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ctr = {}
        idxs = {}
        for idx, ch in enumerate(t):
            idxs.setdefault(ch, []).append(idx)
        for ch in s:
            for i, idx in enumerate(idxs.get(ch, [])[::-1]):
                
                if idx == 0:
                    ctr[idx] = ctr.get(idx, 0) + 1
                else:
                    ctr[idx] = ctr.get(idx, 0) + ctr.get(idx-1, 0)

        
        return ctr.get(len(t) -1, 0)