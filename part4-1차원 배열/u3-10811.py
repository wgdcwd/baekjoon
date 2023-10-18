n, m = map(int, input().split(" "))
basket = [i for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split(" "))
    basket = (
        basket[:a] + basket[b : a - 1 : -1] + basket[b + 1 :]
    )  # basket[b : a - 1 : -1] == basket[a : b + 1][::-1]
print(*basket[1:])
