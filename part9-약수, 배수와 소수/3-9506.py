import math

while True:
    n = int(input())
    if n == -1:
        break
    arrf = []
    arrb = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i != 0:
            continue
        arrf.append(i)
        arrb.append(n // i)

    if arrf[-1] == arrb[-1]:
        arrf = arrf[:-1]
    arrb = arrb[1:]
    arr = arrf[:] + arrb[::-1]

    if sum(arr) != n:
        print(str(n) + " is NOT perfect.")
    else:
        print(str(n) + " = ", end="")
        for i in arr[:-1]:
            print(str(i) + " + ", end="")
        print(arr[-1])
