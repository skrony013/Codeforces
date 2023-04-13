import math

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    gcd = math.gcd(2, k)
    if n % gcd == 0:
        print("YES")
    else:
        print("NO")