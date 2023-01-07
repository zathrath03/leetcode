class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        excess_gas = [g - c for g, c in zip(gas, cost)]
        if sum(excess_gas) < 0: return -1
        
        start = 0
        running_sum = 0
        
        for index in range(len(excess_gas)):
            running_sum += excess_gas[index]
            if running_sum < 0:
                running_sum = 0
                start = index + 1
        
        return start