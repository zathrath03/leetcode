class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = len(picture)
        cols = len(picture[0])
        row_sums = [0] * rows
        col_sums = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if picture[row][col] == "B":
                    row_sums[row] += 1
                    col_sums[col] += 1

        count = 0
        for row in range(rows):
            for col in range(cols):
                if picture[row][col] == "B" and row_sums[row] == 1 and col_sums[col] == 1:
                    count += 1
                    
        return count