def comb(arr, k, m, n) :
    if m < k :
        print(*arr[1:])
        return
    for i in range(arr[k - 1], n + 1) :
        arr[k] = i
        comb(arr, k+1, m, n)
        arr[k] = 0

n, m = map(int, input().split())
arr = [1 for i in range(m + 1)]
comb(arr, 1, m, n)