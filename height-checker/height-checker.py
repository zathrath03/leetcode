class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedCopyOfHeights = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != sortedCopyOfHeights[i]:
                count += 1

        return count