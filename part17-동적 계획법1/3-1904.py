def tile(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    if n in arr :
        return arr[n]
    arr[n] = (tile(n-1) + tile(n-2)) % 15746
    return arr[n]

n = int(input())
arr = {}
print(tile(n))

#재귀한도오류