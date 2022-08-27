class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftPtr = 0
        rightPtr = len(nums) - 1
        sortedSquares = [None] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[leftPtr]) > abs(nums[rightPtr]):
                sortedSquares[i] = nums[leftPtr] * nums[leftPtr]
                leftPtr += 1
            else:
                sortedSquares[i] = nums[rightPtr] * nums[rightPtr]
                rightPtr -= 1
        
        return sortedSquares
