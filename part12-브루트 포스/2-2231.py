n = input()
ans = 0
for i in range(int(n) - len(n) * 10, int(n)) :
    if i < 1 :
        continue
    suma = 0
    temp = list(map(int, list(str(i))))
    suma +=  sum(temp)
    suma += int(i)
    if suma == int(n) :
        ans = i
        break
print(ans)