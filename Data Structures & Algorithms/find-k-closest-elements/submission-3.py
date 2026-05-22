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
            elif med > 0 and abs(arr[med-1] - x) <= abs(arr[med+k-1] -x):
                right = med -1
            else:
                left = med
                right = left
        

        return arr[left:left+k]