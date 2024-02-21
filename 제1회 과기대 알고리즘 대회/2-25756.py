n = int(input())
arr = list(map(int, input().split(" ")))
V = 0
for i in range(n):
    V = 1 - (1 - V) * (1 - arr[i] / 100)
    print(V * 100)
