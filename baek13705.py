from sys import stdin
import math
A, B, C = map(int, stdin.readline().rstrip().split(" "))

x=0

fprime = lambda x : A*x+B*math.sin(x % 2*math.tau)-C
f = lambda x : A/2*x**2-B*math.cos(x)-C*x

print(fprime(x))
for i in range(10000000):
    x = x-0.00001*fprime(x)
    print(x)

print(x)
print(round(x,6))