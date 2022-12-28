from sys import stdin
N, R = map(int, stdin.readline().split(" "))
p = 1000000007

def pow(a,t,p):
    if t == 0:
        return 1
    elif t == 1:
        return a % p
    else:
        cache = pow(a, t//2, p)
        return (cache * cache * a ** (t % 2)) % p

up = 1
down = 1
for i in range(1, R+1):
    up *= (N + 1 - i) % p
    up %= p

    down *= i % p
    down %= p

rst = (up * pow(down, p-2, p)) % p
print(rst)