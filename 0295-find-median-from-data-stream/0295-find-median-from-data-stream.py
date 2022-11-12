from bisect import bisect

class MedianFinder:

    def __init__(self):
        self.datastream = []

    def addNum(self, num: int) -> None:
        if self.datastream:
            self.datastream.insert(bisect(self.datastream, num), num)
        else:
            self.datastream.append(num)

    def findMedian(self) -> float:
        length = len(self.datastream)
        midpoint = length // 2
        if length % 2 == 0:
            return (self.datastream[midpoint] + self.datastream[midpoint - 1]) / 2
        else:
            return float(self.datastream[midpoint])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()