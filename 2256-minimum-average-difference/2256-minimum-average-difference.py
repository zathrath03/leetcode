class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_avg_dif = (100001,)
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
            avg_dif = abs(left_avg - right_avg)
            if avg_dif < min_avg_dif[0]:
                min_avg_dif = (avg_dif, i)

        return min_avg_dif[1]