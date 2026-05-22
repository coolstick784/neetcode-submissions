class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
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
                    if left > idx2+1 and l == nums[left-1]:
                        left += 1
                        continue
                    if right < len(nums) - 1 and r == nums[right+1]:
                        right -= 1
                        continue
                    if l + r < goal:
                        left += 1
                    elif l + r > goal:
                        right -= 1
                    else:
                        out.append([n1, n2, l, r])
                        left += 1
                        right -= 1

        return out