'''
I did NOT come up with this soltion.
I understand it now that I see it,
but I was not able to come up with it.
'''

from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        values = self.diff.values()
        for delta in values:
            cur += delta
            res = max(cur, res)
        return res
