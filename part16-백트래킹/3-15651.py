def permutation(arr, k, m, n) :
    if m == k :
        print(*arr)
        return
    for i in range(1, n + 1) :
        arr[k] = i
        permutation(arr, k+1, m, n)
        arr[k] = 0

n, m = map(int, input().split())
arr = [0 for i in range(m)]
permutation(arr, 0, m, n)