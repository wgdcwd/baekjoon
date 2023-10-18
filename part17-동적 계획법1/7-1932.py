n = int(input())
dp = [[0 for i in range(j)] for j in range(1, n + 1)]

dp[0][0] = int(input())
for i in range(1, n) :
    temp = list(map(int, input().split()))
    for j in range(i + 1) :
        if j == 0 :
            dp[i][j] = dp[i -1][j] + temp[j]
        elif j == i :
            dp[i][j] = dp[i - 1][j - 1] + temp[j]
        else :
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + temp[j]
print(max(dp[n - 1]))