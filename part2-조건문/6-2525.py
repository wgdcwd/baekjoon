h, m = map(int, input().split())
n = int(input())
m = m + n
h = h + m//60
m = m % 60
h = h % 24

print(h, m)