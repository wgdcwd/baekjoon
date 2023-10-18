testCase = int(input())
arr = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
arr[0] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(1,15) :
    for j in range(1,15) :
        arr[i].append(arr[i-1][j] + arr[i][j-1])
for i in range(testCase) :
    k = int(input())
    n = int(input())
    print(arr[k][n])
