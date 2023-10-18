ans = 0
n = int(input())
temp = n
while True :
    if temp < 10 :
        temp = temp * 11
    else :
        temp = 10 * (temp % 10) + (((temp % 10) + (temp // 10)) % 10)
    ans += 1
    if temp == n :
        break
print(ans)