def isHan(n) :
    if (n//100) - ((n//10)%10) == ((n//10)%10) - n%10 :
        return True
    return False


n = int(input())

if n < 100 :
    print(n)
elif n == 1000 :
    print(144)
else :
    cnt = 99
    for i in range(100, n+1) :
        if isHan(i) == True :
            cnt += 1
    print(cnt)
