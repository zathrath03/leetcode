class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for i in range(len(matrix[0])):
                if row[i] > target:
                    break
                elif row[i] == target:
                    return True
