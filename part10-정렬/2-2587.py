arr = []
sum = 0
for i in range(5) :
    arr.append(int(input()))
    sum += arr[i]
arr.sort()
print(int(sum/5))
print(arr[2])