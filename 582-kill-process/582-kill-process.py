class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        output = set()
        output.add(kill)
        hash_map = defaultdict(set)
        
        for p, pp in zip(pid, ppid):
            hash_map[pp].add(p)
        
        children = hash_map[kill]
        while children:
            output |= children
            childs = set()
            for child in children:
                child_children = hash_map[child]
                if type(child_children) == set:
                    childs |= child_children
                else:
                    childs.add(child_children)
            children = childs

        return list(output)