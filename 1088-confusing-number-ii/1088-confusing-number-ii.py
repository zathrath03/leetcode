class Solution:
    def confusingNumberII(self, N: int) -> int:
        confusingDigits = [0, 1, 6, 8, 9]
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        S = str(N)
        Ls = len(S)
        halfLen = Ls // 2
        oddLen = bool(Ls % 2)

        ans = 2
        for l in range(2, Ls):
            ans += 4 * (5 ** (l - 1) - 5 ** (l // 2 - 1) * (3 if l % 2 == 1 else 1))

        def calc(idx):
            thisNum = int(S[idx])
            if thisNum > 8:
                searchIdx = 4
            elif thisNum > 6:
                searchIdx = 3
            elif thisNum > 1:
                searchIdx = 2
            elif thisNum == 1:
                searchIdx = 1
            else:
                searchIdx = 0
            if idx == Ls - 1:
                return searchIdx + (confusingDigits[searchIdx] == int(S[idx]))
            smallerNum = searchIdx - 1 if idx == 0 else searchIdx
            res = smallerNum * 5 ** (Ls - idx - 1)
            if idx < halfLen:
                res -= smallerNum * 5 ** (halfLen - idx - 1) * (3 if oddLen else 1)
            if idx == halfLen and oddLen:
                res -= 3 if thisNum > 8 else (2 if thisNum > 1 else (1 if thisNum > 0 else 0))
            if confusingDigits[searchIdx] == int(S[idx]):
                res += calc(idx + 1)
            return res

        ans += calc(0)
        firstHalfRevNum = 0
        for i in range(halfLen - 1, -1, -1):
            if S[i] not in mapping:
                return ans
            firstHalfRevNum = firstHalfRevNum * 10 + int(mapping[S[i]])
        if oddLen:
            if S[halfLen] in {"0", "1", "8"} and int(S[halfLen + 1:]) >= firstHalfRevNum:
                ans -= 1
        elif int(S[halfLen:]) >= firstHalfRevNum:
                ans -= 1
        return ans