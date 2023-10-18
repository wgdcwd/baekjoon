def isSelfNum(n) :
    ans = True
    for i in range(n - len(str(n)) * 9, n) :
        if i < 1 :
            continue
        if (i + sumDigit(i)) == n :
            ans = False
            break
    return ans

def sumDigit(n) :
    ans = 0
    while n :
        ans += n%10
        n = n //10
    return ans

for i in range(1, 10001) :
    if isSelfNum(i) == True :
        print(i)