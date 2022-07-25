class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len("%i" % num) % 2 == 0:
                count += 1
        return count
    