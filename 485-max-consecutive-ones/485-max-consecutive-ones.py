class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        temp_consecutive_ones = 0

        for num in nums:
            if num:
                temp_consecutive_ones += 1
                max_consecutive_ones = max(max_consecutive_ones, temp_consecutive_ones)
            else:
                temp_consecutive_ones = 0

        return max_consecutive_ones
