from fractions import Fraction
n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n) :
    if arr[0] % arr[i] == 0 :
        print(str(arr[0] // arr[i]) + "/1")
    else :
        print(Fraction(arr[0], arr[i]))