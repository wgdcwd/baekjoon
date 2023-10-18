arr = []
for i in range(9) :
    arr = arr + list(map(int, input().split()))
max = max(arr)
ind = arr.index(max)
print(max)
print(ind//9 + 1, ind%9 + 1)