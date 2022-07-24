class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for i in range(len(row)):
                if row[i] == target:
                    return True
                elif row[i] > target:
                    break
