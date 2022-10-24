class Solution:
    def maxLength(self, arr: list[str]) -> int:
        result = [""]
        longest = 0
        for word in arr:
            for i in range(len(result)):
                new_res = result[i] + word
                if len(new_res) == len(set(new_res)):
                    result.append(new_res)
                    longest = max(longest, len(new_res))
        return longest
