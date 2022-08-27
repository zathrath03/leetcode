class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        values = [False] * (len(nums) + 1)
        values[0] = True
        disappearedNumbers = []
        
        for val in nums:
            values[val] = True

        for index, present in enumerate(values):
            if not present:
                disappearedNumbers.append(index)
            
        return disappearedNumbers