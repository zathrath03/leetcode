class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        index = len(nums) // 2
        
        if nums[index] == target:
            return index
        if nums[index] > target:
            return self.search(nums[:index], target)
        else:
            rtn = self.search(nums[index+1:], target)
            if rtn == -1:
                return rtn
            else:
                return rtn + index + 1
