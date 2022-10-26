class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return any(number + int(str(number)[::-1]) == num for number in range(num + 1))