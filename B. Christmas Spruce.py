from collections import defaultdict

n=int(input())
tree = defaultdict(list)

for i in range(n-1):
    c = int(input())
    tree[c].append(i+2)

for key in tree.keys():
    c = 0

    for node in tree[key]:
        if node not in tree:
            c+=1

    if c < 3:
        print("No")
        exit()

print("Yes")
