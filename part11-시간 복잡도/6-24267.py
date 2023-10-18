# n이 5일때
# i는 1 2 3
# j는 234 34 4
# k는 345455 455 5
# 즉 n이5면 sum(3~1) + sum(2~1) + sum(1~1) (n+1) * n / 2
n = int(input())
print(int(n * (n - 1) * (n - 2) / 6))
print(3)
