class Solution:
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        line_point_map = self.getLines(points)
        self.distributePointsToLines(points, line_point_map)
        return self.findMaxPoints(line_point_map)

    def getLines(self, points):
        line_point_map = defaultdict(set)
        for pt1 in points:
            for pt2 in points:
                if pt1 == pt2:
                    continue
                self.addEquationsToMap(pt1, pt2, line_point_map)
        return line_point_map

    def distributePointsToLines(self, points, line_point_map):
        for point in points:
            for line in line_point_map.keys():
                self.addPointToLine(point, line, line_point_map)

    def addPointToLine(self, point, line, line_point_map):
        if self.isOnVerticalLine(point[0], line) or self.isOnLine(point, line):
            line_point_map[line].add(tuple(point))

    def isOnLine(self, point, line):
        m, b = line
        x, y = point
        return y == m * x + b

    def isOnVerticalLine(self, x, line):
        m, b = line
        return m == float(inf) and b == x

    def findMaxPoints(self, line_point_map):
        most_points = 0
        for pts in line_point_map.values():
            most_points = max(most_points, len(pts))
        return most_points

    def addEquationsToMap(self, pt1, pt2, line_point_map):
        equation = self.getEquation(pt1, pt2)
        line_point_map[equation].add(tuple(pt1))
        line_point_map[equation].add(tuple(pt2))

    def getEquation(self, p1, p2):
        if self.isVerticalLine(p1, p2):
            return float(inf), p1[0]
        m = self.getSlope(p1, p2)
        b = self.getYIntercept(p1, m)
        return m, b

    def isVerticalLine(self, p1, p2):
        return p1[0] == p2[0]

    def getYIntercept(self, p1, m):
        return p1[1] - m * p1[0]

    def getSlope(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)
