# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n+1
        firstBad = n+1
        
        while left < right:
            n = (right + left) // 2
            if isBadVersion(n):
                right = n
                firstBad = min(firstBad, n)
            else:
                left = n + 1

        return firstBad