class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = set(nums)
        
        if len(nums) < 3:
            thirdMax = max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            thirdMax = max(nums)
        
        return thirdMax
