n = int(input())
dp = []
dp.append(list(map(int, input().split())))
for i in range(1, n) :
    a, b, c = map(int, input().split())
    a = min(dp[i - 1][1], dp[i - 1][2]) + a
    b = min(dp[i - 1][0], dp[i - 1][2]) + b
    c = min(dp[i - 1][0], dp[i - 1][1]) + c
    dp.append([a, b, c])
print(min(dp[n - 1]))