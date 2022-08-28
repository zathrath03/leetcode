class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [0]
        
        for i in range(len(nums)):
            prefixSums.append(prefixSums[i] + nums[i])

        for i in range(len(nums)):
            if prefixSums[i] == prefixSums[-1] - prefixSums[i] - nums[i]:
                return i
        
        return -1
