class Solution:
    def mapLeftPushes(self, dominoes: str) -> list:
        left = [False] * len(dominoes)
        pushedLeft = False
        for i in reversed(range(len(dominoes))):
            push = dominoes[i]
            if push == 'R':
                pushedLeft = False
            elif pushedLeft or push =='L':
                left[i] = True
                pushedLeft = True
        return left
    
    def mapRightPushes(self, dominoes: str) -> list:
        right = [False] * len(dominoes)
        pushedRight = False
        for i, push in enumerate(dominoes):
            if push == 'L':
                pushedRight = False
            elif pushedRight or push == 'R':
                right[i] = True
                pushedRight = True
        return right
    
    def propogatePushesWithoutConflicts(self, left, right, length):
        output = ['.'] * length
        
        for i, (l, r) in enumerate(zip(left, right)):
            if l and not r:
                output[i] = 'L'
            elif r and not l:
                output[i] = 'R'
        
        return output
    
    def propogateConflicts(self, output):
        i = 0
        while i < len(output):
            if output[i] == 'R':
                i += 1
                if i < len(output) and output[i] == 'R':
                    continue
                start = i
                while i < len(output) and output[i] == '.':
                    i += 1
                end = i
                sub_len = end - start
                for j in range(start, start + sub_len//2):
                    output[j] = 'R'
                for j in range(end - 1, start + sub_len//2 - 1 + (sub_len & 1), -1):
                    output[j] = 'L'
            i += 1
        return output
    
    def pushDominoes(self, dominoes: str) -> str:

        right = self.mapRightPushes(dominoes)
        left = self.mapLeftPushes(dominoes)
        output = self.propogatePushesWithoutConflicts(left, right, len(dominoes))
        output = self.propogateConflicts(output)

        return "".join(output)