n, g = input().split(" ")
game_dic = {"Y": 1, "F": 2, "O": 3}
n = int(n)
people = set()
for i in range(n):
    people.add(input())
print(len(people) // game_dic[g])
