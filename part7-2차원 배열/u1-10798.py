max_len = 0
arr = []
for i in range(5):
    arr.append(input())
    max_len = max(max_len, len(arr[i]))
for i in range(max_len):
    for j in range(5):
        if len(arr[j]) <= i:
            pass
        else:
            print(arr[j][i], end="")
