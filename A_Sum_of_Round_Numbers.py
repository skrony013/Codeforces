T = int(input())
for t in range(T):
    n = int(input())
    temp = 1
    ans = []
    while n > 0:
        d = int(n % 10)
        r = int(d * temp)
        if r > 0:
            ans.append(r)
        temp = temp * 10
        n = n // 10
    print(len(ans))
    print(' '.join(map(str, ans)))