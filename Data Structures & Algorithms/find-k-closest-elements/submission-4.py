class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr
        left = 0
        right = len(arr) - k 
        while left < right:
            med = (left + right) // 2
            if med+k < len(arr) and abs(arr[med] - x) > abs(arr[med+k] - x):
                left = med + 1
            else:
                right = med
        

        return arr[left:left+k]