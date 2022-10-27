from collections import defaultdict
from typing import Iterator


class Solution:
    def largestOverlap(self, img1: list[list[int]],
                       img2: list[list[int]]) -> int:
        one, two = self.get_coordinates_of_ones(img1, img2)
        shift_counts: defaultdict = defaultdict(int)
        output = 0
        for shift in self.get_shifts(one, two):
            shift_counts[shift] += 1
            output = max(output, shift_counts[shift])
        return output

    def get_shifts(self,
                   one: list[tuple[int, int]],
                   two: list[tuple[int, int]]
                   ) -> Iterator[tuple[int, int]]:
        for pt1 in one:
            for pt2 in two:
                yield (pt2[0] - pt1[0], pt2[1] - pt1[1])

    def get_coordinates_of_ones(self,
                                img1: list[list[int]],
                                img2: list[list[int]]
                                ) -> tuple[list[tuple[int, int]],
                                           list[tuple[int, int]]]:
        n = len(img1)
        one = []
        two = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one.append((i, j))
                if img2[i][j] == 1:
                    two.append((i, j))
        return one, two