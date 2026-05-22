class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pre = []
        cur = 0
        for n in nums:
            cur += n
            pre.append(cur)
        ctr = Counter(pre)
        res = ctr[k]
        for p in pre:
            goal = k + p
            ctr[p] -= 1
            res += ctr[goal]
        return res