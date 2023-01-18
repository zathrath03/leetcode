class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = cur_max = cur_min = 0
        max_sum = min_sum = nums[0]
        for num in nums:
            cur_max = max(num, num + cur_max)
            max_sum = max(cur_max, max_sum)
            cur_min = min(num, num + cur_min)
            min_sum = min(cur_min, min_sum)
            total += num
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
