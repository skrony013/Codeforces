t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().strip().split(' ')))[:N]
    A.sort()
    if len(A) == 1:
        print("Yes")
    else:
        c = 0
        for n in range(len(A) - 1):
            if A[n] == A[n + 1]:
                print("No")
                break
            else:
                c = c + 1
        if c > 0:
            print("Yes")
