n, k = map(int, input().split())
if k > (n - k) :
    k = n - k

five, two = 0, 0

for i in range(n, n - k, - 1) :
    twotemp, fivetemp = i, i
    while twotemp % 2 == 0 and twotemp != 0 :
        two += 1
        twotemp //= 2
    while fivetemp % 5 == 0 and fivetemp != 0 :
        five += 1
        fivetemp //= 5

for i in range(1, k + 1) :
    twotemp, fivetemp = i, i
    while twotemp % 2 == 0 and twotemp != 0 :
        two -= 1
        twotemp //= 2
    while fivetemp % 5 == 0 and fivetemp != 0 :
        five -= 1
        fivetemp //= 5

print(min(two, five))