class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashm = {}
        res = []
        for idx1, n1 in enumerate(nums[:-1]):
            for i2, n2 in enumerate(nums[idx1+1:]):
                idx2 = idx1+i2 + 1
                target = -1 * (n1 + n2)
                print(n1, n2, target)
                print(hashm)
                if target in hashm and sorted([n1, n2, target]) not in res:
                    res.append(sorted([n1, n2, target]))
            hashm[n1] = idx1

        return res