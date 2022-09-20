class Solution:
    def parseString(self, string: str):
        files = []
        contents = []

        splits = string.split()
        directory = splits[0]
        splits = splits[1:]

        for file in splits:
            file_and_contents = file.removesuffix(')').split('(')
            files.append(file_and_contents[0])
            contents.append(file_and_contents[1])

        return directory, files, contents

    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        contents_locations = {}
        output = []

        for string in paths:
            directory, files, contents = self.parseString(string)
            for i, content in enumerate(contents):
                contents_locations[content] = (
                    contents_locations.get(content, [])
                    + [f'{directory}/{files[i]}'])
        
        for files in contents_locations.values():
            if len(files) > 1:
                output.append(files)
        return output
