t = int(input())
for i in range(t):
    g = 'codeforces'
    ch = input()
    flag = 0
    for item in g:
        if item == ch:
            flag = 1
    if flag == 1:
        print("Yes")
    else:
        print("No")
