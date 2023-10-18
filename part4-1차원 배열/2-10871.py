n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n) :
    if x > arr[i] :
        print(arr[i], end=' ')