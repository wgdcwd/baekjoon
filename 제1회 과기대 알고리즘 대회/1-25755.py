w, n = input().split(" ")
n = int(n)
arr = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    for j in range(n):
        if temp[j] == 1 or temp[j] == 8:
            pass
        elif temp[j] == 2:
            temp[j] = 5
        elif temp[j] == 5:
            temp[j] = 2
        else:
            temp[j] = "?"
    arr.append(temp[:])
if w == "L" or w == "R":
    for i in range(n):
        arr[i] = arr[i][::-1]
else:
    arr = arr[::-1]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
