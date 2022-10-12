class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        for i in range(len(nums)-2):
            c, b, a = nums[i], nums[i+1], nums[i+2]
            if c < a + b:
                return a + b + c
        return 0