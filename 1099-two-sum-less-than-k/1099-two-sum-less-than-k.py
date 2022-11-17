class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        rgt = min(bisect_left(nums, k), len(nums) - 1)
        lft = 0
        closest_sum = -1
        
        while lft < rgt:
            total = nums[lft] + nums[rgt]
            if total >= k:
                rgt -= 1
            else:
                closest_sum = max(total, closest_sum)
                lft += 1

        return closest_sum
        