class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = running_sum = total_sum = 0
        
        for i in range(len(gas)):
            excess_gas = gas[i] - cost[i]
            total_sum += excess_gas
            running_sum += excess_gas
            if running_sum < 0:
                running_sum = 0
                start = i + 1
        
        return start if total_sum >= 0 else -1