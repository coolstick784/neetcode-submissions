#transpose then flip
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if c <= r:
                    continue
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1
