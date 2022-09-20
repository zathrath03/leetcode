class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for file in files:
                file_name, _, content = file.partition('(')
                maps[content].append(f'{directory}/{file_name}')
        return [x for x in maps.values() if len(x) > 1]