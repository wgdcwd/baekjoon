n, max = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
ans = 0
for i in range(0, n) :
    sum += arr[i]
    for j in range(i+1, n) :
        sum += arr[j]
        for k in range(j+1, n) :
            sum += arr[k]
            if sum <=max and sum > ans :
                ans = sum
            sum -= arr[k]
        sum -= arr[j]
    sum -= arr[i]

print(ans)