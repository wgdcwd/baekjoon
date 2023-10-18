def queen(a, b, c, k, n, ans) :
    if k == n :
        ans[0] += 1
        return
    for i in range(n) :
        if a[i] == 1 :
            continue
        if b[i + k] == 1 :
            continue
        if c[k - i + n - 1] == 1 :
            continue
        a[i] = 1
        b[i + k] = 1
        c[k - i + n - 1] = 1
        queen(a, b, c, k + 1, n ,ans)
        a[i] = 0
        b[i + k] = 0
        c[k - i + n - 1] = 0

        

n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(2 * n - 1)]
c = [0 for i in range(2 * n - 1)]
ans = [0]
queen(a, b, c, 0, n, ans)
print(ans[0])