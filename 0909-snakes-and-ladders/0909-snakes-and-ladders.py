class Solution:
    def snakesAndLadders(self, board):
        N, lvl = len(board), 0

        line = [0]
        for row in range(N)[::-1]:
            line.extend(board[row] if (N - row) % 2 else board[row][::-1])

        Q, visit, target = deque([1]), set(), N * N
        next_options = lambda n: range(n + 1, min(n + 6, target) + 1)

        while Q:
            lvl += 1
            for _ in range(len(Q)):
                cur = Q.popleft()
                if cur in visit: continue
                visit.add(cur)

                for nxt in next_options(cur):
                    if line[nxt] != -1: nxt = line[nxt]
                    if nxt == target: return lvl
                    Q.append(nxt)
        return -1