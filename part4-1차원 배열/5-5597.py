arr = []
n = 30
for i in range(n+1) :
    arr.append(False)
for i in range(n-2) :
    arr[int(input())] = True
for i in range(1, 31) :
    if arr[i] == False :
        print(i)
