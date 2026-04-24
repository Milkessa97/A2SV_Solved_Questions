class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        def inRange(bomb1,bomb2):
            x_dist = bomb1[0] - bomb2[0]
            y_dist = bomb1[1] - bomb2[1]
            return pow(x_dist,2) + pow(y_dist,2) <= pow(bomb1[2],2)

        for i in range(len(bombs)):
            parent = tuple([bombs[i][0],bombs[i][1],bombs[i][2],i])
            for j in range(len(bombs)):
                if i != j and inRange(bombs[i],bombs[j]):
                    child = tuple([bombs[j][0],bombs[j][1],bombs[j][2],j])
                    graph[parent].append(child)

        max_bombs = 0

        def dfs(node):
            visited.add(node[3])
            for child in graph[node]:
                if child[3] not in visited:
                    dfs(child)

        for idx in range(len(bombs)):
            visited = set()
            check = tuple([bombs[idx][0],bombs[idx][1],bombs[idx][2],idx])
            dfs(check)
            max_bombs = max(max_bombs, len(visited))

        return max_bombs       