import math
def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

n = int(input())
ans = 0
arr = list(map(int, input().split()))
for i in arr :
    if isPrime(i) == True :
        ans += 1

print(ans)