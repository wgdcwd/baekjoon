import math
def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

a = int(input())
b = int(input())
min = 0
sum = 0
for i in range(a,b+1) :
    if isPrime(i) == True :
        if min == 0 :
            min = i
        sum += i

if sum == 0 :
    print(-1)
else :
    print(sum)
    print(min)