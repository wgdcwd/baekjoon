n = int(input())
for i in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    #원2가 원1보다 반지름이 크거나 같음
    if r1 > r2 :
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1

    dp = ((y2 - y1) ** 2) + ((x2 - x1) ** 2)
    
    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    
    elif dp == (r1 + r2) ** 2 :
        print(1)

    elif dp == (r2 - r1) ** 2 :
        print(1)

    elif dp > (r2 - r1) ** 2 and dp < (r1 + r2) ** 2 :
        print(2)
    
    else :
        print(0)
