class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        excess_gas = [g - c for g, c in zip(gas, cost)]
        
        start = running_sum = total_sum = 0
        
        for index in range(len(excess_gas)):
            total_sum += excess_gas[index]
            running_sum += excess_gas[index]
            if running_sum < 0:
                running_sum = 0
                start = index + 1
        
        return start if total_sum >= 0 else -1