

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        start_ptr = 0
        end_ptr = k
        max_length = 0
        char_count = {char: s[:k].count(char) for char in set(s[:k])}
        char_count_values = char_count.values()
        
        while end_ptr < len(s):
            char_count[s[end_ptr]] = char_count.get(s[end_ptr], 0) + 1
            end_ptr += 1
            
            most_chars = max(char_count_values)
            other_chars = sum(char_count_values) - most_chars
            window_width = end_ptr - start_ptr
            
            if other_chars <= k:
                max_length = max(max_length, window_width)
            else:
                char_count[s[start_ptr]] -= 1
                start_ptr += 1
            
        return max_length
                
        # create a window on s
        
        # add the character in the window to char_count
        # if the sum of the counts for the characters that don't have the max count is less than k:
        # # expand the window to the right (within limits of s)
        # # add the new character to the count
        # else:
        # # replace max_length is window length is longer
        # # slide to the right
        # # remove the character from the left
        # # add the new character on the right