class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for val in nums:
            if val != 0:
                nums[i] = val
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        