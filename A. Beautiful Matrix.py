m, n = 0, 0
for i in range(5):
    line = [int(x) for x in input().split()]
    for j in range(5):
        if line[j] != 0:
            m = i + 1
            n = j + 1
            break
if m >= 3:
    m -= 3
else:
    m = 3 - m
if n >= 3:
    n -= 3
else:
    n = 3 - n
print(m+n)
