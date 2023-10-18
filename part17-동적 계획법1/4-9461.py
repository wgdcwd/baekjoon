def padovan(n) :
    if len(arr) > n :
        return arr[n]
    arr.append(padovan(n-1) + padovan(n-5))
    return arr[n]

n = int(input())
arr = [0,1,1,1,2,2,3,4,5,7,9]
for i in range(n) :
    print(padovan(int(input())))