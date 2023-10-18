def make_team(k, n) :
    if k == n//2 :
        cal(n)
        return

    for i in range(n) :
        if i <= team[-1] :
            continue
        team.append(i)
        make_team(k + 1, n)
        team.pop()

def cal(n) :
    team1 = set(team[1:])
    team2 = set([i for i in range(n)]) - team1
    t1s, t2s = 0, 0
    for i in team1 :
        for j in team1 :
            t1s += arr[i][j]
    for i in team2 :
        for j in team2 :
            t2s += arr[i][j]
    sub = abs(t2s - t1s)
    if sub < min[0] :
        min[0] = sub


n = int(input())
team = [-1]
arr = []
for i in range(n) :
    arr.append(list(map(int, input().split())))
min = [2000]
make_team(0, n)
print(min[0])