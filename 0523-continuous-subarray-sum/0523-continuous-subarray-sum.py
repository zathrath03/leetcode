class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # if sum(nums[i:j])%k == 0, then sum(nums[:i])%k == sum(nums[:j])%k
        remainders = {0: 0}

        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            if remainder not in remainders:
                remainders[remainder] = i + 1
            elif remainders[remainder] < i:
                return True
        return False