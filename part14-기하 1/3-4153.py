arr = [0, 0, 0]
while True:
    arr[0], arr[1], arr[2] = map(int, input().split())
    if arr[0] == 0 :
        break
    arr.sort()
    if (arr[0] * arr[0] + arr[1] * arr[1]) == arr[2] * arr[2] :
        print("right")
    else :
        print("wrong")