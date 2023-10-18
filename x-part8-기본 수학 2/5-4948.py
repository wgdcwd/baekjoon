import math
def isPrime(n) :
    if n == 1 or n == 0 :
        return False
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

arr = []
for i in range(0, 123456 * 2 + 1) :
    if isPrime(i) == True :
        arr.append(True)
    else :
        arr.append(False)

while True :
    n = int(input())
    if n == 0 :
        break
    ans = 0
    for i in range(n+1, 2*n+1) :
        if arr[i] == True :
            ans += 1
    print(ans)
