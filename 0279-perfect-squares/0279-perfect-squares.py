class Solution:
    def numSquares(self, n: int) -> int:

        def is_divided_by(n, count):
            if count == 1:
                return n in squares

            for square in squares:
                if (is_divided_by(n - square, count - 1)):
                    return True

        squares = {i ** 2 for i in range(int(sqrt(n)), 0, -1)}

        for count in range(1, 4):
            if is_divided_by(n, count):
                return count

        return 4  # Lagrange's four-square theorem shows that 4 is the max