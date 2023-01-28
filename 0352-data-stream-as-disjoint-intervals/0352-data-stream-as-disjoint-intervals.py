from sortedcontainers import SortedSet

class SummaryRanges:
    
    def __init__(self):
        self.__integers_seen = SortedSet()

    def addNum(self, value: int) -> None:
        self.__integers_seen.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.__integers_seen: return [[]]
        
        intervals = [];
        left = right = -1
        
        for value in self.__integers_seen:
            if left < 0:
                left = right = value
            elif value == right + 1:
                right = value
            else:
                intervals.append([left, right])
                left = right = value
        
        intervals.append([left, right])
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()