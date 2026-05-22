class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_map = {}
        res = set()
        for idx1, n1 in enumerate(nums[:-1]):
            for i2, n2 in enumerate(nums[idx1+1:]):
                idx2 = idx1+i2+1
                goal = -1 * (n1+n2)
                if goal in hash_map:
                    to_add = tuple(sorted([n1, n2, goal]))
                    res.add(to_add)
            hash_map[n1] = idx1
        return list(res)
