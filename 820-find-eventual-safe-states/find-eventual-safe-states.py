class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        grey = set()
        black = set()
        tree = defaultdict(list)

        def dfs(root):
            
            grey.add(root)
            for node in graph[root]:
                if node not in grey and node not in black:
                    if not dfs(node):
                        return False
                elif node in grey:
                    return False
            grey.remove(root)
            black.add(root)
            return True
        
        for root in range(len(graph)):
            dfs(root)
        return sorted(list(black))