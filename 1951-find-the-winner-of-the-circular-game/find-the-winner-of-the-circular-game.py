class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        check = deque([x for x in range(1,n+1)])
        count = 1
        while len(check) > 1:
            if count == k:
                check.popleft()
                count = 1
            else:
                check.append(check.popleft())
                count += 1
        return check[0]

