class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        return len({*nums} - {0})