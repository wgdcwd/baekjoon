import math
def isPrime(n) :
    if n == 1 or n == 0 :
        return False
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

arr = []
for i in range(0,  10001) :
    if isPrime(i) == True :
        arr.append(True)
    else :
        arr.append(False)

n = int(input())
for i in range(n) :
    k = int(input())
    temp = k // 2
    while True :
        if arr[temp] == True and arr[k - temp] == True :
            print(temp, k - temp)
            break
        else :
            temp -= 1

