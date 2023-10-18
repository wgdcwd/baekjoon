n = int(input())
arr = list(map(int, input().split()))
ans = sum(arr) * 100 / max(arr) / n
print(ans)