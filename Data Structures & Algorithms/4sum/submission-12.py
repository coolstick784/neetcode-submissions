class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = set()
        for idx1, n1 in enumerate(nums):
            if idx1 > 0 and n1 == nums[idx1-1]:
                continue
            for idx2 in range(idx1+1, len(nums)):
                n2 = nums[idx2]
                if idx2 > idx1+1 and n2 == nums[idx2-1]:
                    continue
                left = idx2+1
                right = len(nums) - 1
                goal = target - n1 - n2
                while left < right:
                    l = nums[left]
                    r = nums[right]
                    if l + r < goal:
                        left += 1
                    elif l + r > goal:
                        right -= 1
                    else:
                        out.add((n1, n2, l, r))
                        left += 1
                        right -= 1
        res = []
        for a, b, c, d in out:
            res.append([a, b, c, d])
        return res