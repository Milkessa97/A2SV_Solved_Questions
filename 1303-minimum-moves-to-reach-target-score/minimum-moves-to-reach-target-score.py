class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1:
            while maxDoubles:
                if target != 1 and target % 2==1:
                    count += 1
                    target-= 1
                else:
                    target = int(target / 2)
                    maxDoubles -= 1
                    count+=1
                if target == 1:
                    break
            if not maxDoubles:
                break
        count += target - 1
        return count