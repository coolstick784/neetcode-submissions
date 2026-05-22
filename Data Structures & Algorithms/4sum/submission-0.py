class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        hashm = {}
        for idx1, n1 in enumerate(nums[:-2]):
            for i2, n2 in enumerate(nums[idx1+1:-1]):
                idx2 = idx1 + i2 + 1
                for i3, n3 in enumerate(nums[idx2+1:]):
                    idx2 = idx2 + i3 + 1
                    cur = n1+n2 + n3
                    goal = target - (n1+n2+n3)
                    if goal in hashm:
                        n_sorted = tuple(sorted([n1, n2, n3, goal]))
                        res.add(n_sorted)
            hashm[n1] = idx1
        return [li for li in res]

