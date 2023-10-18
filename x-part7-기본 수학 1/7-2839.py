n = int(input())
a = n // 5
b = 0
while a>=0 :
    if (n - 5 * a) % 3 == 0 :
        b = (n - 5 * a) // 3
        break
    a -= 1
if a < 0 :
    print(-1)
else :
    print(a+b)