class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for column in range(len(matrix[0])):
                if row[column] == target:
                    return True
                elif row[column] > target:
                    break