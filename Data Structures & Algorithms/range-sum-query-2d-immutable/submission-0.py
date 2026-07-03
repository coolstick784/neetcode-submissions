from functools import lru_cache
import copy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.og_matrix = copy.deepcopy(matrix)
        self.matrix = matrix
        for row in range(len(matrix)-1, -1, -1):
            for col in range(len(matrix[0])-1, -1, -1):
                if row < len(matrix) - 1:
                    self.matrix[row][col] += self.matrix[row+1][col]
                if col < len(matrix[0]) - 1:
                    self.matrix[row][col] += self.matrix[row][col+1]
                if row < len(matrix) -1 and col < len(matrix[0]) - 1:
                    self.matrix[row][col] -= self.matrix[row+1][col+1]
        print("matrix", self.matrix)
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        out = self.matrix[row1][col1] 
        if row2 < len(self.matrix) - 1:
            out -= self.matrix[row2+1][col1]
        if col2 < len(self.matrix[0]) - 1:
            out -= self.matrix[row1][col2+1]
        if row2 < len(self.matrix)-1 and col2 < len(self.matrix[0]) - 1:
            out += self.matrix[row2+1][col2+1]
        return out

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)