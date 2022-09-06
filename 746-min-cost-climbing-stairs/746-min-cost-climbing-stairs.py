class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_down = two_down = 0
        for i in range(2, len(cost)+1):
            temp = one_down
            one_down = min(one_down + cost[i-1], two_down + cost[i-2])
            two_down = temp
        return one_down