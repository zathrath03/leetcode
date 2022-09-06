class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        cache = {0: cost[0], 1: cost[1]}
        for i in range(2, len(cost)):
            cache[i] = cost[i] + min(cache[i-1], cache[i-2])
            
        return min(cache[len(cost)-1], cache[len(cost)-2])