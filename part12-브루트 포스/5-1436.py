n = int(input())
i = 0
cnt = 0
while i < n :
    cnt += 1
    while True :
        if "666" in str(cnt) :
            i += 1
            break
        cnt += 1
print(cnt)