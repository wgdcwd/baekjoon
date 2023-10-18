def w_first(arr, i, j) :
    cnt = 0
    for q in range(8) :
        for w in range(8) :
            if (q+w) % 2 == 0 :
                if arr[i + q][j + w] == 'B' :
                    cnt += 1
            else :
                if arr[i + q][j + w] == 'W' :
                    cnt += 1
    return cnt

def b_first(arr, i, j) :
    cnt = 0
    for q in range(8) :
        for w in range(8) :
            if (q+w) % 2 == 0 :
                if arr[i + q][j + w] == 'W' :
                    cnt += 1
            else :
                if arr[i + q][j + w] == 'B' :
                    cnt += 1
    return cnt

def cal(arr, i, j) :
    w = w_first(arr, i, j)
    b = b_first(arr, i, j)
    if w < b :
        return w
    else :
        return b


# n = 세로, m = 가로 arr[n][m] 형식
n, m = map(int, input().split())

arr = []
for i in range(n) :
    arr.append(input())
min = n * m
for i in range(0, n - 7) :
    for j in range(0, m - 7) :
        temp = cal(arr, i, j)
        if temp < min :
            min = temp
print(min)