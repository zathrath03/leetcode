class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddPtr = 0
        evenPtr = len(nums) - 1
        
        while evenPtr > oddPtr:
            while evenPtr > oddPtr and nums[oddPtr] % 2 == 0:
                oddPtr += 1
            while evenPtr > oddPtr and nums[evenPtr] % 2 == 1:
                evenPtr -= 1
            if evenPtr > oddPtr:
                nums[oddPtr], nums[evenPtr] = nums[evenPtr], nums[oddPtr]
                oddPtr += 1
                evenPtr -= 1
        
        return nums