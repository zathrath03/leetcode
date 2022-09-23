class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        output = []

        for interval in intervals:
            a, b, c, d = interval[0], interval[1], toBeRemoved[0], toBeRemoved[1]
            if b <= c or a >= d:
                output.append(interval)
            elif a >= c and b <= d:
                pass
            elif a < c and b <= d:
                output.append([a, c])
            elif a >= c and b > d:
                output.append([d, b])
            elif a < c and b > d:
                output.append([a, c])
                output.append([d, b])

        return output
    