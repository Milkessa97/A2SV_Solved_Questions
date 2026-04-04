class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        main_diag = set()
        sub_diag = set()

        count = 0
        
        def backtrack(i):
            nonlocal count
            if i == n:
                count+=1
                return
            
            for j in range(n):
                
                if j not in cols and (i-j) not in main_diag and (i+j) not in sub_diag:
                    cols.add(j)
                    main_diag.add(i-j)
                    sub_diag.add(i+j)

                    backtrack(i+1)

                    cols.remove(j)
                    main_diag.remove(i-j)
                    sub_diag.remove(i+j)

        backtrack(0)
        return count
