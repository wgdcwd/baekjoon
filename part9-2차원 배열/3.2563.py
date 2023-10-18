arr = [[0 for i in range(100)] for j in range(100)]
for i in range(int(input())) :
    a, b = map(int, input().split())
    for j in range(10) :
        for k in range(10) :
            arr[a+j][b+k] = 1
            ans = 0
for i in range(100) :
    ans += arr[i].count(1)
print(ans)