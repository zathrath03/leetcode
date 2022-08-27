class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftPtr = 0
        rightPtr = len(nums) - 1
        sortedSquares = [None] * len(nums)
        sortedSquaresPtr = rightPtr
        
        while leftPtr <= rightPtr:
            if abs(nums[leftPtr]) > abs(nums[rightPtr]):
                sortedSquares[sortedSquaresPtr] = nums[leftPtr] * nums[leftPtr]
                leftPtr += 1
            else:
                sortedSquares[sortedSquaresPtr] = nums[rightPtr] * nums[rightPtr]
                rightPtr -= 1
            sortedSquaresPtr -= 1
        
        return sortedSquares
