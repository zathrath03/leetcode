class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        avg_dif = {}
        left_sum = 0
        right_sum = sum(nums)
        
        for i in range(n):
            left_sum += nums[i]
            right_sum -= nums[i]
            left_avg = left_sum // (i + 1)
            if i != n - 1:
                right_avg = right_sum // (n - 1 - i)
            else:
                right_avg = 0
            avg_dif.setdefault(abs(left_avg - right_avg), i)
            
        return avg_dif[min(avg_dif)]