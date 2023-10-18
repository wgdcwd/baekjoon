import sys
n = int(input())
arr = []
for i in range(n) :
    arr.append(int(sys.stdin.readline().strip()))
arr = sorted(arr)
for i in range(n) :
    sys.stdout.write(str(arr[i]) + "\n")