txt = input()


def inversion(part):
    return "".join(part[i] for i in range(len(part)-1, -1, -1))

minString = "z" * 50
for i in range(1, len(txt)-1):
    for j in range(i+1, len(txt)):
        minString = min(minString, inversion(txt[:i])+inversion(txt[i:j])+inversion(txt[j:]))


print(minString)
