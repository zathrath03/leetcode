class Solution:
    cache = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        uniquePaths = self.cache.get((m,n), self.cache.get((n,m)))
        if uniquePaths:
            return uniquePaths
        if m == n:
            uniquePaths = 2 * self.cache.get((m-1,n), self.cache.get((m,n-1), 0))
        if uniquePaths:
            self.cache[(m,n)] = uniquePaths
            return uniquePaths
        
        self.cache[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.cache[(m,n)]