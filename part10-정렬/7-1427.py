n = input()
cnt = [0 for i in range(10)]
for i in range(len(n)) :
    cnt[int(n[i])] += 1
for i in range(10) :
    print(str(9-i) * cnt[9-i], end="")
    