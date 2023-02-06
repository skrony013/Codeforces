t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().strip().split(' ')))[:N]
    A.sort()

    c = 0
    for n in range(len(A) - 1):
        if A[n] < A[n + 1]:
            continue
        else:
            c = c+1
    if c == 0:
        print("Yes")
    else:
        print("No")
