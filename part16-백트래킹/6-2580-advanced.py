def sudoku(k, n):
    if k == n :
        return True    
    a, b = zeroIndex[k]
    for i in range(1, 10) :
        if i in column[b] :
            continue
        if i in row[a] :
            continue
        if i in box[a//3][b//3]:
            continue
        
        column[b].add(i)
        row[a].add(i)
        box[a//3][b//3].add(i)
        answer.append(i)
        if sudoku(k+1, n) :
            return True
        answer.pop()
        
        column[b].remove(i)
        row[a].remove(i)
        box[a//3][b//3].remove(i)
    return False

arr = []
zeroIndex = []
for i in range(9) :
    arr.append(list(map(int, input().split())))

column = [{-1} for i in range(9)]
row = [{-1} for i in range(9)]
box = [[{-1}, {-1}, {-1}], [{-1}, {-1}, {-1}], [{-1}, {-1}, {-1}]]
for i in range(9) :
    for j in range(9) :
        if arr[i][j] == 0 :
            zeroIndex.append([i, j])
        else :
            column[j].add(arr[i][j])
            row[i].add(arr[i][j])
            box[i//3][j//3].add(arr[i][j])

answer = []

sudoku(0, len(zeroIndex))

for i in range(len(answer)) :
    arr[zeroIndex[i][0]][zeroIndex[i][1]] = answer[i]
for i in range(9) :
    for j in range(9) :
        print(arr[i][j], end = " ")
    print()