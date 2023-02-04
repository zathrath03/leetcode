class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l2 = len(s2)
        l1 = len(s1)

        if l1 > l2:
            return False

        hp1 = {i: 0 for i in string.ascii_lowercase}
        hp2 = hp1.copy()

        for s in s1:
            hp1[s] += 1

        for i in range(l1):
            char = s2[i]
            hp2[char] += 1

        for i in range(l1,l2):
            if hp1 == hp2:
                return True
            char_to_remove = s2[i-l1]
            char_to_add = s2[i]
            hp2[char_to_remove] -= 1
            hp2[char_to_add] += 1

        if hp1 == hp2:
            return True

        return False
