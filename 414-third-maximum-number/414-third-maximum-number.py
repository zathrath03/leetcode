class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = sorted(set(nums))
        
        if len(nums) < 3:
            thirdMax = max(nums)
        else:
            thirdMax = nums[-3]
        
        return thirdMax
            