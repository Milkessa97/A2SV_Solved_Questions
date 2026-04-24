class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(node, path = []):
            nonlocal paths
            path.append(node)
            if node != len(graph) - 1:
                for child in graph[node]:
                    dfs(child, path)
            else:
                paths.append(path.copy())
            path.pop()
        
        dfs(0)
        return paths