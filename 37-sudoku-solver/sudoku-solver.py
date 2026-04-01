class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def sec(i,j):
            if i<3:
                if j<3:
                    return 0
                elif j<6:
                    return 3
                else:
                    return 6
            elif i>=3 and i<6:
                if j<3:
                    return 1
                elif j<6:
                    return 4
                else:
                    return 7
            else:
                if j<3:
                    return 2
                elif j<6:
                    return 5
                else:
                    return 8

        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        sets = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sets[sec(i,j)].add(board[i][j])
        def backtrack(i,j):
            if i == 9:
                return True

            if j + 1 < 9:
                new_i = i
                new_j = j+1
            else:
                new_i = i+1
                new_j = 0

            if board[i][j] == '.':
                for num in map(str,range(1,10)):
                    
                    if num not in row[i] and num not in col[j] and num not in sets[sec(i,j)]:
                        board[i][j] = num
                        row[i].add(num)
                        col[j].add(num)
                        sets[sec(i,j)].add(num)
                        
                        if backtrack(new_i,new_j):
                            return True

                        board[i][j] = '.'
                        row[i].remove(num)
                        col[j].remove(num)
                        sets[sec(i,j)].remove(num)
            else:
                if backtrack(new_i,new_j):
                    return True
            return False

        backtrack(0,0)