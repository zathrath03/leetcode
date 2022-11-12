from heapq import heappush, heappop, heappushpop

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        lo, hi = self.heaps
        if len(lo) == len(hi):
            num = heappushpop(hi, num)
            heappush(lo, -num)
        else:
            num = heappushpop(lo, -num)
            heappush(hi, -num)
        
    def findMedian(self) -> float:
        lo, hi = self.heaps
        if len(lo) == len(hi):
            return (hi[0] - lo[0]) / 2
        return -lo[0]