from itertools import combinations


class Solution:
    
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        maxLength = 0
        dp = [[0] * (len(nums1)+1) for _ in range(len(nums1)+1)]
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 == num2:
                    length = dp[i][j] + 1
                    maxLength = max(length, maxLength)
                    dp[i+1][j+1] = length
        
        return maxLength