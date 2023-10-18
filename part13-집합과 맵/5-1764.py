import sys
n, m = map(int, input().split())
s1 = set()
s2 = set()
for i in range(n) :
    s1.add(sys.stdin.readline().strip())
for i in range(m) :
    s2.add(sys.stdin.readline().strip())
arr = list(s1 & s2)
arr.sort()
print(len(arr))
for i in arr :
    print(i)