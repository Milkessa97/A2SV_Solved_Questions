class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        count = 0

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row,col):
            nonlocal dirs, count
            if (row,col) in visited or grid[row][col] == "0":
                return False
            
            if grid[row][col] == "1":
                visited.add((row,col))

                for x,y in dirs:
                    new_row, new_col = row + x, col + y
                    if inbound(new_row,new_col) and grid[new_row][new_col] == "1":
                        dfs(new_row,new_col)
                    new_row, new_col = row - x, col - y
            return True

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(row,col):
                    count += 1
                    
        return count