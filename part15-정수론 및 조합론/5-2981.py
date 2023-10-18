import math
import sys
n = int(input())
arr = []
for i in range(n) :
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()
subarr = []
for i in range(n - 1) :
    subarr.append(arr[i+1] - arr[i])
gcd = math.gcd(*subarr)
ans = set()
for i in range(2, int(gcd ** (1/2)) + 1) :
        if gcd % i == 0 :
            ans.add(i)
            ans.add(gcd // i)
ans.add(gcd)
ans.discard(1)
ans = list(ans)
ans.sort()
print(*ans)