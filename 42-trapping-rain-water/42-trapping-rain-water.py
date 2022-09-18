class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        max_from_left = [None] * n
        max_from_right = [None] * n
        ans = cur_left_max = cur_right_max = 0

        for i in range(n):
            cur_left_max = max(cur_left_max, height[i])
            cur_right_max = max(cur_right_max, height[n-1-i])
            max_from_left[i] = cur_left_max
            max_from_right[n-1-i] = cur_right_max
        for i in range(n):
            ans += (min(max_from_left[i], max_from_right[i]) - height[i])

        return ans
