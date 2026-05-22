class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ctr = Counter(nums)
        out = set()
        for idx1, n1 in enumerate(nums):
            ctr[n1] -= 1
            old_ctr = ctr.copy()
            for idx2 in range(idx1+1, len(nums)):
                n2 = nums[idx2]
                ctr[n2] -= 1
                old_ctr_2 = ctr.copy()
                for idx3 in range(idx2+1, len(nums)):
                    n3 = nums[idx3]
                    ctr[n3] -= 1
                    goal = target - n1 - n2 - n3
                    if ctr.get(goal, 0) > 0:
                        cur = sorted([n1, n2, n3, goal])
                        out.add((cur[0], cur[1], cur[2], cur[3]))
                ctr = old_ctr_2.copy()
            ctr = old_ctr.copy()
        res = []
        for a, b, c, d in out:
            res.append([a, b, c, d])
        return res