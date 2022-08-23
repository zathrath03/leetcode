class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        i = 1
        while i < len(nums):
            if temp == nums[i]:
                nums.remove(nums[i])
            else:
                temp = nums[i]
                i += 1