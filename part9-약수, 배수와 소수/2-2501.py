import math

n, k = map(int, input().split(" "))
arrf = []
arrb = []

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i != 0:
        continue
    arrf.append(i)
    arrb.append(n // i)

if arrf[-1] == arrb[-1]:
    arrf = arrf[:-1]
arr = arrf[:] + arrb[::-1]

if len(arr) >= k:
    print(arr[k - 1])
else:
    print(0)
