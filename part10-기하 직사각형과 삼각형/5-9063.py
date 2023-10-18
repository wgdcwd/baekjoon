n = int(input())
x = []
y = []
for i in range(n):
    xt, yt = map(int, input().split(" "))
    x.append(xt)
    y.append(yt)
print((max(x) - min(x)) * (max(y) - min(y)))
