max = int(input())
dp = {max : 0}
for i in range(max - 1, 0, -1) :
    a = dp[i + 1]
    if i * 2 <= max :
        temp = dp[i * 2]
        if temp < a :
            a = temp
    if i * 3 <= max :
        temp = dp[i * 3]
        if temp < a :
            a = temp
    dp[i] = a + 1

print(dp[1])