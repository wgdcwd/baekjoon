a1, a0 = map(int, input().split(" "))
c = int(input())
n0 = int(input())
if c - a1 < 0:
    print(0)
elif (c - a1) * n0 >= a0:
    print(1)
else:
    print(0)
