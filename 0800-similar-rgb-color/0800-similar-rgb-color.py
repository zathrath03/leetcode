from typing import Iterator

class Solution:
    def similarRGB(self, color: str) -> str:
        def separate_colors(color: str) -> Iterator[str]:
            for i in range(1, 6, 2):
                yield color[i:i+2]

        def find_nearest_double_color(color: str) -> str:
            doubles = {0: "00", 17: "11", 34: "22", 51: "33", 68: "44",
                       85: "55", 102: "66", 119: "77", 136: "88", 153: "99",
                       170: "aa", 187: "bb", 204: "cc", 221: "dd", 238: "ee",
                       255: "ff"}
            color_int = int("0x" + color, 16)
            delta = {abs(k-color_int): v for k, v in doubles.items()}

            return delta[min(delta)]

        output = "#"

        for c in separate_colors(color):
            output += find_nearest_double_color(c)

        return output