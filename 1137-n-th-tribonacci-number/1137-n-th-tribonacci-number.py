class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
