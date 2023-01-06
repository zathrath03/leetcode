class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
    
        for count, cost in enumerate(costs):
            coins -= cost
            if coins < 0:
                return count

        return len(costs)
