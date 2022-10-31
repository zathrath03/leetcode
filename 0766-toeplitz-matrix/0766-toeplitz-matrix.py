class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        for row in range(num_rows - 1):
            if matrix[row][:num_cols - 1] != matrix[row + 1][1:]:
                return False
        return True