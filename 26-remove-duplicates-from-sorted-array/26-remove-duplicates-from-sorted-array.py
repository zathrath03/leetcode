class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = -101
        i = 0
        while i < len(nums):
            if temp == nums[i]:
                nums.remove(nums[i])
            else:
                temp = nums[i]
                i += 1