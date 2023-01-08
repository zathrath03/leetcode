class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3: return len(points)
        lines = self.getLines(points)
        self.distributePointsToLines(points, lines)
        return self.findMaxPoints(lines)

    def getLines(self, points):
        lines = defaultdict(set)
        for pt1 in points:
            for pt2 in points:
                if pt1 is pt2: continue
                self.addEquationsToLines(pt1, pt2, lines)
        return lines

    def distributePointsToLines(self, points, lines):
        for pt in points:
            for m, b in lines.keys():
                if m == float(inf) and b == pt[0]:
                    lines[(m, b)].add(tuple(pt))
                if pt[1] == m * pt[0] + b:
                    lines[(m, b)].add(tuple(pt))

    def findMaxPoints(self, lines):
        most_points = 0
        for pts in lines.values():
            most_points = max(most_points, len(pts))
        return most_points

    def addEquationsToLines(self, pt1, pt2, lines):
        equation = self.getEquation(pt1, pt2)
        lines[equation].add(tuple(pt1))
        lines[equation].add(tuple(pt2))

    def getEquation(self, p1, p2):
        if p2[0] == p1[0]: return float(inf), p2[0]
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return m, b
