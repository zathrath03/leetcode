class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])
        ptr = [0] * num_rows
        largest_current_value = mat[0][0]
        current_element = [0] * num_rows

        while True:
            for row in range(num_rows):
                while (ptr[row] < num_cols
                       and mat[row][ptr[row]] < largest_current_value):
                    ptr[row] += 1
                if (col := ptr[row]) == num_cols:
                    return -1
                largest_current_value = current_element[row] = mat[row][col]
                if len(set(current_element)) == 1:
                    return largest_current_value
