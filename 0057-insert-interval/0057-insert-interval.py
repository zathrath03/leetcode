class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals: return [newInterval]

        self.intervals = intervals
        self.newInterval = newInterval

        unpacked_intervals = list(itertools.chain.from_iterable(intervals))

        start_index = bisect.bisect_left(unpacked_intervals, newInterval[0])
        end_index = bisect.bisect_right(unpacked_intervals, newInterval[1], lo=start_index)

        new_interval = self.get_new_interval(start_index, end_index)

        return self.generate_output(start_index, end_index, new_interval)

    def get_new_interval(self, start_index: int, end_index: int) -> list[int]:
        start_value = self.get_start_value(start_index)
        end_value = self.get_end_value(end_index)
        return [start_value, end_value]

    def generate_output(self, start_index, end_index, new_interval):
        output = self.intervals[:start_index // 2]
        output.append(new_interval)
        return output + self.intervals[(end_index + 1) // 2:]

    def get_start_value(self, start_index: int) -> int:
        if self.isOdd(start_index):
            return self.intervals[start_index // 2][0]
        else:
            return self.newInterval[0]

    def get_end_value(self, end_index: int) -> int:
        if self.isOdd(end_index):
            return self.intervals[end_index // 2][1]
        else:
            return self.newInterval[1]

    def isOdd(self, n: int) -> bool:
        return n & 1
