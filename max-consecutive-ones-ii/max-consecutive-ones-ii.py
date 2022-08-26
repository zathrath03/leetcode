class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroIndexes = []
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndexes.append(i)
        
        if len(zeroIndexes) == len(nums):
            maxOnes = 1
        elif len(zeroIndexes) < 2:
            maxOnes = len(nums)
        else:
            maxOnes = max(zeroIndexes[1], len(nums) - zeroIndexes[-2] - 1)
            for i in range(2, len(zeroIndexes)):
                maxOnes = max(maxOnes, zeroIndexes[i] - zeroIndexes[i-2] - 1)
            
        return maxOnes