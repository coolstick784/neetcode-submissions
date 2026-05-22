class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        hash_map = {}
        res = set()
        for idx1, n1 in enumerate(nums[:-2]):
            for i2, n2 in enumerate(nums[idx1+1:-1]):
                idx2 = idx1 + i2 + 1
                for i3, n3 in enumerate(nums[idx2+1:]):
                    idx3 = idx2+1+i3
                    goal = target - n1 - n2 - n3
                    if goal in hash_map:
                        to_add = tuple(sorted([n1, n2, n3, goal]))
                        res.add(to_add)

            hash_map[n1] = idx1
        return list(res)