class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, n in enumerate(nums):
            goal = target-n
            if goal in hash_map:
                return [hash_map[goal], idx]
            hash_map[n] = idx