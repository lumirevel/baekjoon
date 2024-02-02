a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))

upper = a*d + c*b
lower = b*d

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

g = gcd(upper, lower)

print(f"{upper//g} {lower//g}")