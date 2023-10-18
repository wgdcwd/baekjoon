x = [0, 0, 0]
y = [0, 0, 0]
x[0], y[0] = map(int, input().split())
x[1], y[1] = map(int, input().split())
x[2], y[2] = map(int, input().split())

x.sort()
y.sort()

if x[0] == x[1] :
    print(x[2], end = " ")
else :
    print(x[0], end = " ")


if y[0] == y[1] :
    print(y[2])
else :
    print(y[0])