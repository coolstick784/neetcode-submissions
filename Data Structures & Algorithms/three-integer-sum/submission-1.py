class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashm = {}
        res = set()
        out_strs = []
        for idx1, n1 in enumerate(nums[:-1]):
            for i2, n2 in enumerate(nums[idx1+1:]):
                idx2 = idx1+i2 + 1
                target = -1 * (n1 + n2)
                c_str = str(n1) + str(n2) + str(target)
                if target in hashm :
                    res.add(tuple(sorted([n1, n2, target])))
            hashm[n1] = idx1

        return [li for li in res]