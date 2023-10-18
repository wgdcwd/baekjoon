n = int(input())
arr = list(map(int, input().split()))
dp = []
dp.append(arr[0])
for i in range(1, n):
    if dp[i - 1] >= 0 :
        dp.append(dp[i - 1] + arr[i])
    else :
        dp.append(arr[i])

print(max(dp))