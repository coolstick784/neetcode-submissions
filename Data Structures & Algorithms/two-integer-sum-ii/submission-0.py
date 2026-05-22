# if it's >, we will never use that right again
# if it's <, we will never use that left again

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            l = numbers[left]
            r = numbers[right]
            if l + r > target:
                right -= 1
            elif l + r < target:
                left += 1
            else:
                return [left+1, right+1]