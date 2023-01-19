class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l = 0
        y = reader.length() - 1

        while l < y:
            third = (y - l) // 3
            r = l + third
            x = y - third

            match reader.compareSub(l, r, x, y):
                case 0:
                    l = r + 1
                    y = x - 1
                case 1:
                    y = r
                case -1:
                    l = x
        return l
