n = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n) :
    temp = 0
    for j in range(0, i) :
        if arr[i] <= arr[j] :
            continue
        if dp[j] > temp :
            temp = dp[j]
    dp[i] = temp + 1
print(max(dp))