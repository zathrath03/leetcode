class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        memo = {}
        mask = 0
        for v in piles:
            mask = (mask << 3) + v

        @cache
        def play(mask):
            for i in range(len(piles)):
                t = (mask >> (3 * i)) & 7
                if not t:
                    continue
                for k in range(1, t + 1):
                    a = k << (3 * i)
                    if not mask - a or not play(mask - a):
                        return True
            return False

        return play(mask)
