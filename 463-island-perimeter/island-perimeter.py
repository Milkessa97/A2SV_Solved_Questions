class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        answer = 0
        directions = [(-1,0), (0,-1)]

        def dfs(row,col):
            nonlocal answer
            if row == len(grid):
                return
            if inbound(row,col):
                if grid[row][col] == 1:
                    answer += 4
                    visited.add((row,col))
                
                    for x,y in directions:
                        new_row, new_col = row + x, col + y
                        if inbound(new_row,new_col) and (new_row,new_col) in visited:
                            answer -= 2

                dfs(row, col + 1)
            else:
                dfs(row + 1, 0)

        dfs(0,0)
        return answer