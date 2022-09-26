class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality_map = defaultdict(set)
        inequality_map = defaultdict(set)
        for equation in equations:
            c1 = equation[0]
            c2 = equation[3]
            if equation[1] == '=':
                equality_map[c1] |= (equality_map[c2] | {c1, c2})
                equality_map[c2] |= (equality_map[c1] | {c1, c2})
                for val in equality_map[c1]:
                    equality_map[c1] = equality_map[val] = equality_map[val].union(equality_map[c1])
                for val in equality_map[c2]:
                    equality_map[c2] = equality_map[val] = equality_map[val].union(equality_map[c2])
            else:
                if c1 == c2:
                    return False
                if equals := equality_map.get(c1):
                    if c2 in equals:
                        return False
                if equals := equality_map.get(c2):
                    if c1 in equals:
                        return False
                inequality_map[c1].add(c2)
                inequality_map[c2].add(c1)
        
        for key, val in inequality_map.items():
            if key in equality_map:
                for v in val:
                    if v in equality_map[key]:
                        return False

        return True