def cal(str) :
    stack = 0
    ans = 0
    for i in range(len(str)) :
        if str[i] == 'X' :
            stack = 0
            continue
        stack += 1
        ans += stack
    return ans

n = int(input())
for i in range(n) :
    print(cal(input()))

