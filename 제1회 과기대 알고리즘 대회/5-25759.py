n = int(input())
arr = list(map(int, input().split(" ")))
up_or_down = -1  # 증가할때 1 감소할때 0
ans = []
if arr[0] < arr[1]:
    up_or_down = 1
else:
    up_or_down = 0

ans.append(arr[0])
for i in range(1, n - 1):
    if arr[i] == arr[i + 1]:
        continue
    if arr[i] < arr[i + 1]:
        if up_or_down == 1:
            continue
        else:
            ans.append(arr[i])
            up_or_down = 1
    else:
        if up_or_down == 0:
            continue
        else:
            ans.append(arr[i])
            up_or_down = 0

ans.append(arr[n - 1])
sum = 0
for i in range(len(ans) - 1):
    sum += (ans[i] - ans[i + 1]) ** 2
print(sum)
