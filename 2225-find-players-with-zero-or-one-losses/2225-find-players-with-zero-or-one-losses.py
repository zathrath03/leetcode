class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        undefeated, one_loss, losers = set(), set(), set()
        for winner, loser in matches:
            if winner not in losers and winner not in one_loss:
                undefeated.add(winner)
            if loser in losers:
                continue
            if loser in undefeated:
                undefeated.remove(loser)
            if loser in one_loss:
                one_loss.remove(loser)
                losers.add(loser)
            else:
                one_loss.add(loser)
        return [sorted(undefeated), sorted(one_loss)]