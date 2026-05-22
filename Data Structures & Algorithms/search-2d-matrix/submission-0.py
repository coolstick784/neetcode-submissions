import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        while up < down -1:
            med = (up + down) // 2
            if matrix[med][0] == target:
                return True
            if matrix[med][0] < target:
                up = med
            if matrix[med][0] > target:
                down = med - 1
        for r in set({up, down}):
            row = matrix[r]
            if row[bisect.bisect(row, target)-1] == target:
                return True
        return False