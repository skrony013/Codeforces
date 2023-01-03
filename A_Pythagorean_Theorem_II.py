def Result(N):
    cnt = 0
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            for c in range(b, N + 1):
                if (a * a) + (b * b) == c * c:
                    cnt += 1
    print(cnt)


p = int(input())
Result(p)
