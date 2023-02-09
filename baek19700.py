from sys import stdin
max_N = 500000
N = int(stdin.readline())
people = []
for _ in range(N):
    people.append(tuple(map(int, stdin.readline().split(" "))))
people.sort(key=lambda x:x[0], reverse=True)

teams = []
position = [None for _ in range(max_N)]
for person in people:
    if teams:
        length = min(person[1] - 1, len(teams[0]))
        while length and position[length] is None:
            length -= 1
        if length == 0:
            teams.append([person])
            if position[1] is None:
                position[1] = len(teams) - 1
        else:
            teams[position[length]].append(person)

            if position[length + 1] is None:
                position[length + 1] = position[length]

            if position[length] == len(teams) - 1:
                position[length] = None
            elif len(teams[position[length] + 1]) != length:
                position[length] = None
            else:
                position[length] += 1
    else:
        teams.append([person])
        position[1] = 0

print(len(teams))
