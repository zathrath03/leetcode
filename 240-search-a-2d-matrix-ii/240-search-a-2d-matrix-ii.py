class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        for row in matrix:
            for i in range(columns):
                if row[i] == target:
                    return True
                elif row[i] > target:
                    columns = i
                    break
