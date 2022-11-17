class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        closest_sum = -1

        for i, num in enumerate(nums):
            j = bisect_left(nums, k - num, i + 1) - 1
            if j == i:
                break
            closest_sum = max(closest_sum, num + nums[j])

        return closest_sum
