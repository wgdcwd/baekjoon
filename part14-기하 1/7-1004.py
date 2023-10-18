def isIn(x1, y1, x2, y2, r) :
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 < r ** 2 :
        return True
    return False

n = int(input())

for i in range(n) :
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    k = int(input())
    for j in range(k) :
        temp = list(map(int, input().split()))
        startP = isIn(x1, y1, temp[0], temp[1], temp[2])
        endP = isIn(x2, y2, temp[0], temp[1], temp[2])
        if (startP and not endP) or (not startP and endP) :
            ans += 1
    print(ans)
