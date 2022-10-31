class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        for row in range(num_rows - 1):
            last_row = matrix[row][:num_cols - 1]
            curr_row = matrix[row + 1][1:]
            if last_row != curr_row:
                return False
        return True