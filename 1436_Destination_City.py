class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = [paths[i][0] for i in range(len(paths))]
        for path in paths:
            if path[1] not in sources:
                return path[1]
