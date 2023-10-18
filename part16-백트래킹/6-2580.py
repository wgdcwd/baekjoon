def func(arr, blank, column, row, box, k, n, ans) :
    if k == n :
        return True
    a, b = blank[k][0], blank[k][1]
    for i in range(1, 10) :
        if i in column[a] :
            continue
        if i in row[b] :
            continue
        if i in box[a//3][b//3] :
            continue
        ans[k] = i
        if func(arr, blank, column, row, box, k + 1, n, ans) :
            return True
        column[a].remove(i)
        row[b].remove(i)
        box[a//3][b//3].remove(i)

        
    

arr = []
for i in range(9) :
    arr.append(list(map(int, input().split())))

blank = []
column = [{0} for i in range(9)]
row = [{0} for i in range(9)]
box = [[{0} for i in range(3)] for j in range(3)]
for i in range(9) :
    for j in range(9) :
        if arr[i][j] == 0 :
            blank.append([i, j])
        else :
            column[i].add(arr[i][j])
            row[j].add(arr[i][j])
            box[i//3][j//3].add(arr[i][j])

ans = [0 for i in range(len(blank))]
func(arr, blank, column, row, box, 0, len(blank), ans)

for i in range(len(ans)) :
    arr[blank[i][0]][blank[i][1]] = ans[i]
for i in range(9) :
    for j in range(9) :
        print(arr[i][j], end = " ")
    print()
