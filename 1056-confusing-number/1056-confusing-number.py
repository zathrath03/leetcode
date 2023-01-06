class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing_digits = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        n = str(n)
        rotated_n = []

        for digit in n[::-1]:
            if digit not in confusing_digits:
                return False
            rotated_n.append(confusing_digits[digit])

        return "".join(rotated_n) != n
