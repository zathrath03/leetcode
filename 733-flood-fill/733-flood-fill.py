class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        startColor = image[sr][sc]
        
        def floodFillRecurs(sr, sc, newColor):
            image[sr][sc] = newColor
            if (sr-1) >= 0 and image[sr-1][sc] == startColor:
                floodFillRecurs(sr-1, sc, newColor)
            if (sr+1) < len(image) and image[sr+1][sc] == startColor:
                floodFillRecurs(sr+1, sc, newColor)
            if (sc-1) >= 0 and image[sr][sc-1] == startColor:
                floodFillRecurs(sr, sc-1, newColor)
            if (sc+1) < len(image[0]) and image[sr][sc+1] == startColor:
                floodFillRecurs(sr, sc+1, newColor)
        
        floodFillRecurs(sr, sc, color)

        return image