def getCount(n) :
    five = 0
    two = 0
    temp = n
    while n >= 5 and n != 0 :
        five += (n // 5)
        n = n // 5
    n = temp
    while n >= 2 and n != 0 :
        two += (n // 2)
        n = n // 2
    return five, two
        

n, k = map(int, input().split())
arr = [getCount(n), getCount(n - k), getCount(k)]
five = arr[0][0] - arr[1][0] - arr[2][0]
two = arr[0][1] - arr[1][1] - arr[2][1]
print(min(five, two))