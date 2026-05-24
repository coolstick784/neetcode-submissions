class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rowZero = False
        colZero = False
        for r, row in enumerate(matrix):
            for c, el in enumerate(row):
                if el == 0:

                    if c == 0:
                        colZero = True
                    if r == 0:
                        rowZero = True
                    elif r != 0 and c != 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        print("matrix", matrix)
        for r, row in enumerate(matrix):
            for c, el in enumerate(row):
                if r != 0 and c != 0 and (matrix[r][0] == 0 or matrix[0][c] == 0):
                    matrix[r][c] = 0
        print("matrix", matrix)
        for r, row in enumerate(matrix):
            for c, el in enumerate(row):
                if r == 0 and rowZero:
                    matrix[r][c] = 0
                if c == 0 and colZero:
                    matrix[r][c] = 0