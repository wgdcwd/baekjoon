n = int(input())
def fibonacci(n) :
    f = []
    f.append(1)
    f.append(1)
    for i in range(2, n) :
        f.append(f[i - 1] + f[i - 2])
        cnt[1] += 1
    return f[n-1]

n = int(input())
cnt = [0, 0]


print(fibonacci(n), cnt[1])