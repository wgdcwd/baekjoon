n, m = map(int, input().split(" "))
basket = [0 for i in range(n)]
for i in range(m):
    temp = list(map(int, input().split(" ")))
    for j in range(temp[0] - 1, temp[1]):
        basket[j] = temp[2]
print(*basket)
