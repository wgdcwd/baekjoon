def comb(n, r) :
    ans = 1
    for i in range(n, n - r, -1) :
        ans *= i
    for i in range(r, 0, -1) :
        ans //= i
    return ans

n = int(input())
for i in range(n) :
    l, r = map(int, input().split())
    print(comb(r, l))
