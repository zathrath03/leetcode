class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        values = [False] * (len(nums))
        disappearedNumbers = []
        
        for val in nums:
            values[val-1] = True

        for index, present in enumerate(values):
            if not present:
                disappearedNumbers.append(index+1)
            
        return disappearedNumbers