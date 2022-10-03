class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cur_col = ""
        costs = []
        time = 0
        
        for i, color in enumerate(colors):
            if color == cur_col:
                costs.append(neededTime[i])
            else:
                if len(costs) > 1:
                    time += sum(costs) - max(costs)  # write a helper to not need to go through costs twice
                cur_col = color
                costs = [neededTime[i]]
        if len(costs) > 1:
            time += sum(costs) - max(costs)  # write a helper to not need to go through costs twice
                
        return time