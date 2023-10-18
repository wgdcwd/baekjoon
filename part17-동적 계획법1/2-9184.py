def w(a, b, c) :
    if ",".join(map(str, [a,b,c])) in arr :
        return arr[",".join(map(str, [a,b,c]))]
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    if a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)
    if a < b and b < c :
        arr[",".join(map(str, [a,b,c]))] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arr[",".join(map(str, [a,b,c]))]
    else :
        arr[",".join(map(str, [a,b,c]))] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return arr[",".join(map(str, [a,b,c]))]

arr = {}
while True :
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1 :
        break
    print("w(%d, %d, %d) = %d" %(a, b, c, w(a, b, c)))