t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    p = 0
    count = 0
    cycle = -1
    cycle_found = False

    while p < n and k > 0:
        if s[p] == 'L':
            x -= 1
        else:
            x += 1

        k -= 1
        p += 1

        if x == 0:
            count += 1
            if not cycle_found:
                pos = 0
                for i, com in enumerate(s):
                    if com == 'L':
                        pos -= 1
                    else:
                        pos += 1

                    if pos == 0:
                        cycle = i + 1
                        break
                cycle_found = True

            if cycle != -1:
                count += k // cycle
            break

    print(count)
