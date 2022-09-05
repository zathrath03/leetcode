class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        if startColor == newColor:
            return image

        R = len(image) - 1
        C = len(image[0]) - 1

        def floodFillRecurs(r, c):
            if image[r][c] == startColor:
                image[r][c] = newColor
                if r > 0:
                    floodFillRecurs(r-1, c)
                if r < R:
                    floodFillRecurs(r+1, c)
                if c > 0:
                    floodFillRecurs(r, c-1)
                if c < C:
                    floodFillRecurs(r, c+1)

        floodFillRecurs(sr, sc)

        return image
