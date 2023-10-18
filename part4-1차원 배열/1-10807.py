n = int(input())
arr = list(map(int, input().split()))
k = int(input())
ans = 0
for i in range(n) :
    if k == arr[i] :
        ans += 1
print(ans)