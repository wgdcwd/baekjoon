n = int(input())
arr = list(map(int, input().split()))
dpf = [0 for i in range(n)]
dpb = [0 for i in range(n)]

for i in range(n) :
    temp = 0
    for j in range(0, i) :
        if arr[i] <= arr[j] :
            continue
        if dpf[j] > temp :
            temp = dpf[j]
    dpf[i] = temp + 1

arr.reverse()

for i in range(n) :
    temp = 0
    for j in range(0, i) :
        if arr[i] <= arr[j] :
            continue
        if dpb[j] > temp :
            temp = dpb[j]
    dpb[i] = temp + 1

dpb.reverse()

ans = []

for i in range(n) :
    ans.append(dpf[i] + dpb[i] - 1)
print(max(ans))