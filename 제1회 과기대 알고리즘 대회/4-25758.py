ord_a = ord("A")
alphabet_n = 26
n = int(input())
left_list = [[] for i in range(alphabet_n)]
right_list = [[] for i in range(alphabet_n)]
gene = input().split(" ")
ans = set()

for i in range(n):
    left_list[ord(gene[i][0]) - ord_a].append(i)
    right_list[ord(gene[i][1]) - ord_a].append(i)

for i in range(alphabet_n):
    if len(left_list[i]) == 0:
        continue
    for j in range(i, alphabet_n):
        if len(right_list[j]) == 0:
            continue
        if len(left_list[i]) == 1:
            if len(right_list[j]) == 1:
                if left_list[i][0] == right_list[j][0]:
                    continue
        ans.add(chr(j + ord_a))

left_list, right_list = right_list, left_list

for i in range(alphabet_n):
    if len(left_list[i]) == 0:
        continue
    for j in range(i, alphabet_n):
        if len(right_list[j]) == 0:
            continue
        if len(left_list[i]) == 1:
            if len(right_list[j]) == 1:
                if left_list[i][0] == right_list[j][0]:
                    continue
        ans.add(chr(j + ord_a))

ans = list(ans)
ans.sort()
print(len(ans))
print(*ans)
