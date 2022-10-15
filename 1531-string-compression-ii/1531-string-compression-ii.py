class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(idx: int, last_char: str, last_char_count: int, k: int) -> int:
            if k < 0:
                return float('inf')
            if idx == len(s):
                return 0

            delete_char = dp(idx + 1, last_char, last_char_count, k - 1)
            if s[idx] == last_char:
                keep_char = dp(idx + 1, last_char, last_char_count +
                               1, k) + (last_char_count in {1, 9, 99})
            else:
                keep_char = dp(idx + 1, s[idx], 1, k) + 1

            return min(delete_char, keep_char)

        return dp(0, "", 0, k)
