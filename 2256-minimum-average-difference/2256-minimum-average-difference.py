class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_avg_dif = 100001
        left_sum = 0
        right_sum = sum(nums)

        for i, num in enumerate(nums):
            left_sum += num
            right_sum -= num
            left_avg = left_sum // (i + 1)
            if i != n - 1:
                right_avg = right_sum // (n - 1 - i)
            else:
                right_avg = 0
            avg_dif = abs(left_avg - right_avg)
            if avg_dif < min_avg_dif:
                output = i
                min_avg_dif = avg_dif

        return output