class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = running_sum = total_sum = 0
        
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            running_sum += gas[i] - cost[i]
            if running_sum < 0:
                running_sum = 0
                start = i + 1
        
        return start if total_sum >= 0 else -1