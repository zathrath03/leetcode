class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i, val in enumerate(nums):
            rightSum -= val
            if leftSum == rightSum:
                return i
            leftSum += val
            
        return -1
