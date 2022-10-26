class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for val in range(num + 1):
            if val + int(str(val)[::-1]) == num:
                return True