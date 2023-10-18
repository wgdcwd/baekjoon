import sys
c = [0 for i in range(10001)]
n = int(sys.stdin.readline().strip())
for i in range(n) :
    c[int(sys.stdin.readline().strip())] += 1
for i in range(1,10001) :
    for j in range(c[i]) :
        sys.stdout.write(str(i) + "\n")