n = int(input())

for i in range(n) :
    k = int(input())
    arr = {}
    for j in range(k) :
        temp = input().split()
        if temp[1] in arr :
            arr[temp[1]] += 1
        else :
            arr[temp[1]] = 1
    arr = arr.values()
    ans = 1
    for i in arr :
        ans *= (i + 1)
    print(ans - 1)