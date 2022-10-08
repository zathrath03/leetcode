class Solution:    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        n = len(nums)
        for i, num in enumerate(nums):
            lo = i + 1
            hi = n - 1
            while lo < hi:
                total = num + nums[lo] + nums[hi]
                if abs(target - total) < abs(diff):
                    diff = target - total
                    if diff == 0: break
                
                if total < target:
                    lo += 1
                else:
                    hi -= 1

            if diff == 0: break
        return target - diff