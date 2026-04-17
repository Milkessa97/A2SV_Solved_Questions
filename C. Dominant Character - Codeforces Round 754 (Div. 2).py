t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    min_len = float('inf')
    for i in range(n):
        a,b,c = 0,0,0
        for j in range(i, min(i+7,n)):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1
            length = j - i + 1
            if length >= 2 and a > b and a > c:
                min_len = min(min_len, length)
    
    if min_len < float('inf'):
        print(min_len)
    else:
        print(-1)
