a, b = map(int, input().split())

if a < b :
    a, b = b, a

mul = a * b


while True :
    if a % b == 0 :
        gcd = b
        break
    a, b = b, a % b

print(gcd)
print(mul // gcd)

#import math에 gcd(a, b), lcm(a, b) 로 쉽게 풀 수 있다.