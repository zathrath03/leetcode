class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, "".join(str(num) for num in nums).split("0")))
        