n = 42
arr = []
for i in range(n) :
    arr.append(False)
for i in range(10) :
    arr[int(input())%42] = True
print(arr.count(True))