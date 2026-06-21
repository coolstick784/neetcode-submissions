class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pre = {}
        cur = pre
        dicts = {}
        dicts[-1] = pre
        for idx, ch in enumerate(t):
            cur.setdefault(ch, {})
            cur = cur[ch]
            dicts[idx] = cur
            if idx == len(t) - 1:
                cur[True] = t
        ctr = {-1:1}
        for idx in range(len(t)):
            ctr[idx] = 0
        

        for idx, ch in enumerate(s): 
            for i in range(len(t)-1, -2, -1):
                if ctr[i] == 0:
                    continue
                if ch in dicts[i]:
                    ctr[i+1] = ctr.get(i+1, 0) + ctr.get(i, 0) 
            print("idx", idx, "ctr", ctr)

        return ctr.get(len(t) - 1, 0)