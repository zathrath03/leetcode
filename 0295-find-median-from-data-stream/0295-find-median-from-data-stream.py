from bisect import bisect

class MedianFinder:

    def __init__(self):
        self.datastream = []

    def addNum(self, num: int) -> None:
        self.datastream.insert(bisect(self.datastream, num), num)

    def findMedian(self) -> float:
        length = len(self.datastream)
        midpoint = length // 2
        if length & 1:
            return float(self.datastream[midpoint])
        return (self.datastream[midpoint] + self.datastream[midpoint - 1]) / 2