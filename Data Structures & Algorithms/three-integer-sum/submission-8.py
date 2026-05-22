class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        ctr = Counter(nums)
        keys = list(ctr.keys())
        for idx, n in enumerate(keys):
            if n == 0 and ctr[0] >= 3:
                res.append([0,0,0])
            cur = set(keys[idx+1:])
            for idx2, n2 in enumerate(keys[idx+1:]):
                if n2 == -n*2 and ctr[n] >= 2:
                    res.append([n, n, n2])
                if -n2*2 == n and ctr[n2] >= 2:
                    res.append([n, n2, n2])
                if -(n+n2) != n and -(n+n2) != n2 and -(n+n2) in cur:
                    res.append([n, n2, -(n+n2)])
                cur.remove(n2)

            
            del ctr[n]
        return res