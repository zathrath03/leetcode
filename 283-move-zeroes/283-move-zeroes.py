class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for val in nums:
            if val != 0:
                nums[i] = val
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0