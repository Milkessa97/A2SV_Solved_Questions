class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        spots = []
        main_diag = set()
        sub_diag = set()
        cols = set()
        valids = []

        def backtrack(idx):
            nonlocal spots,main_diag,sub_diag,cols,valid
            if len(spots) == n:
                valids.append(spots.copy())
                return

            for i in range(n):
                if idx-i not in main_diag and idx+i not in sub_diag and i not in cols:
                    spots.append(i)
                    main_diag.add(idx-i)
                    sub_diag.add(idx+i)
                    cols.add(i)

                    backtrack(idx+1)

                    spots.pop()
                    main_diag.remove(idx-i)
                    sub_diag.remove(idx+i)
                    cols.remove(i)

        backtrack(0)

        res = []
        for val in valids:
            valid = []
            for spot in val:
                s = ""
                for i in range(n):
                    if i==spot:
                        s+="Q"
                    else:
                        s+="."
                valid.append(s)
            res.append(valid)
        return res