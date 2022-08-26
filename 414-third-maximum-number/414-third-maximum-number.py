class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        if len(nums) < 3:
            thirdMax = max(nums)
        else:
            sortedUniqueNums = sorted(set(nums))
            if len(sortedUniqueNums) < 3:
                thirdMax = max(sortedUniqueNums)
            else:
                thirdMax = sortedUniqueNums[-3]
        
        return thirdMax
            