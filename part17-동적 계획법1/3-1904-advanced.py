arr = [0, 1, 2, 3]
n = int(input())
for i in range(4, n + 1) :
    arr.append((arr[i - 1] + arr[i - 2]) % 15746)
print(arr[n])