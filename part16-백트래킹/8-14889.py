def make_team(k, n) :
    if n == k :
        cal(n)
        return
    
    for i in range(max(team1) + 1, 2 * n) :
        team1.append(i)
        make_team(k + 1, n)
        team1.pop()

def cal(n) :
    team1sum = 0
    team2sum = 0
    for i in team1 :
        for j in team1 :
            if i == -1 or j == -1 :
                continue
            team1sum += arr[i][j]
    for i in range(2*n) :
        for j in range(2*n) :
            if i not in team1 :
                if j not in team1 :
                    team2sum += arr[i][j]
    sub = abs(team2sum - team1sum)
    if sub < min[0] :
        min[0] = sub
    


n = int(input())
arr = []
min = [4000]
for i in range(n) :
    arr.append(list(map(int, input().split())))
team1 = [-1]

make_team(0, n//2)

print(min[0])