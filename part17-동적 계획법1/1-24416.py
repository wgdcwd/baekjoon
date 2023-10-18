def fib(n) :
    if n == 1 or n == 2 :
        cnt[0] += 1
        return 1
    else :
        return fib(n-1) + fib(n - 2)

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

fib(n)
fibonacci(n)
print(cnt[0], cnt[1])