n=int(input())
l=[int(x) for x in input().split()]
l.sort()
check=1
for num in l:
    if check<=num:
        check+=1
print(check-1)
