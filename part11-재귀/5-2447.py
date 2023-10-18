
def star(n) :
    if n == 3 :
        box_3x3 = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
        return box_3x3
    arr = [[" " for i in range(n)] for j in range(n)]
    temp = star(n//3)
    for i in range(n) :
        for j in range(n) :
            arr[i][j] = temp[i%(n//3)][j%(n//3)]

    for i in range(n//3, 2 * n // 3) :
        for j in range(n//3, 2 * n // 3) :
            arr[i][j] = " "
    return arr

n = int(input())
arr = star(n)
for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = "")
    print()