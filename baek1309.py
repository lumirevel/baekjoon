N = int(input())

yes = 2
no = 1
for _ in range(1,N):
    tempYes = yes
    tempNo = no

    yes += tempNo * 2
    no += tempYes
    yes %= 9901
    no %= 9901

print(yes+no)