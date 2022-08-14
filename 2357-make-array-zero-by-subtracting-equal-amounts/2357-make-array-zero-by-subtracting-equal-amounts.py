class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_values = []
        for num in nums:
            if num == 0:
                continue
            elif num not in unique_values:
                unique_values.append(num)
        return len(unique_values)