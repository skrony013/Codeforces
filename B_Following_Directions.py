t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    x = 0
    y = 0
    c = 0
    flag = 0
    for ch in range(0, n):
        if s[ch] == 'U':
            y = y + 1
        elif s[ch] == 'R':
            x = x + 1
        elif s[ch] == 'D':
            y = y - 1
        else:
            x = x - 1
        if x == 1 and y == 1:
            flag = flag + 1
    if flag > 0:
        print("Yes")
    else:
        print("No")
