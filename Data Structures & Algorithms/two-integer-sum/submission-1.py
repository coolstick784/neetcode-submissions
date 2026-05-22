class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, n in enumerate(nums):
            if (target - n) in hash:
                return [hash[target-n], idx]

            hash[n] = idx        