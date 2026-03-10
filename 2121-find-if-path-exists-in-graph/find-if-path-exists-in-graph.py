class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        def dfs(v):
            visited.add(v)
            if v == destination:
                return True
            for ver in adj[v]:
                if ver not in visited:
                    if dfs(ver):
                        return True

        res = dfs(source)
        if res:
            return True
        else:
            return False