n = int(input())
arr = []
for i in range(n) :
    arr.append(int(input()))
dp = [[0, 0, 0] for i in range(n)]
# 0: i-1잔 i잔, 1 : i-2잔 i잔, 2 : i-4, i-3, i잔

if n == 1 :
    print(arr[0])
elif n == 2 :
    print(arr[0] + arr[1])
elif n == 3 :
    print(sum(arr) - min(arr))
elif n == 4 :
    dp[0] = [arr[0], arr[0], arr[0]]
    dp[1] = [arr[0] + arr[1], arr[1], arr[1]]
    dp[2] = [arr[1] + arr[2], arr[0] + arr[2], arr[2]]
    dp[3] = [arr[0] + arr[2] + arr[3], arr[0] + arr[1] + arr[3], arr[0] + arr[3]]
    print(max(max(dp[3]), max(dp[2])))
else :
    dp[0] = [arr[0], arr[0], arr[0]]
    dp[1] = [arr[0] + arr[1], arr[1], arr[1]]
    dp[2] = [arr[1] + arr[2], arr[0] + arr[2], arr[2]]
    dp[3] = [arr[0] + arr[2] + arr[3], arr[0] + arr[1] + arr[3], arr[0] + arr[3]]
    for i in range(4, n) :
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + arr[i]
        dp[i][1] = max(dp[i - 2]) + arr[i]
        dp[i][2] = dp[i - 3][0] + arr[i]
    print(max(max(dp[n - 1]), max(dp[n - 2])))

#계단오르기랑 다른점은 i - 2 까지 신경써줘야 한다는점