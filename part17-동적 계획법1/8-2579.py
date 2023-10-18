n = int(input())
arr = []
for i in range(n) :
    arr.append(int(input()))
dp = [[0, 0] for i in range(n)]
#dp[i][0] 은 1칸 뛰어올라서 온거 dp[i][1]dms 2칸 뛰어올라서 온거

if n == 1 :
    print(arr[0])
elif n == 2 :
    print(arr[0] + arr[1])
else :
    dp[0][0], dp[0][1] = arr[0], arr[0]
    dp[1][0], dp[1][1] = dp[0][0] + arr[1], arr[1]
    for i in range(2, n) :
        dp[i][0] = dp[i - 1][1] + arr[i]
        dp[i][1] = max(dp[i - 2]) + arr[i]
    print(max(dp[n - 1]))