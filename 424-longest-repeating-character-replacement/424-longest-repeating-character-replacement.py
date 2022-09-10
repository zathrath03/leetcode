class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_ptr = 0
        max_length = 0
        char_count = {}
        char_count_values = char_count.values()
        
        for right_ptr in range(len(s)):
            char_count[s[right_ptr]] = char_count.get(s[right_ptr], 0) + 1
            
            most_chars = max(char_count_values)
            other_chars = sum(char_count_values) - most_chars
            window_width = right_ptr - left_ptr + 1
            
            if other_chars <= k:
                max_length = max(max_length, window_width)
            else:
                char_count[s[left_ptr]] -= 1
                left_ptr += 1
            
        return max_length