s1 = input()
s2 = input()
arr = []
dp = []
for i in range(len(s1)) :
    for j in range(len(s2)) :
        if s1[i] == s2[j] :
            arr.append([i, j])

for i in range(len(arr)) :
    temp = 0
    for j in range(0, i) :
        if arr[i][0] <= arr[j][0] :
            continue
        if arr[i][1] <= arr[j][1] :
            continue
        if dp[j] > temp :
            temp = dp[j]
    dp.append(temp + 1)
print(max(dp))