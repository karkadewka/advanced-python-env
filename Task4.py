def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input())
B = int(input())
C = int(input())
D = int(input())

num = A * D
den = B * C

g = gcd(num, den)

print(num // g, "/", den // g)
a = 0
b = 0
R = 5

points = [(1,1), (6,6), (2,2)]
count = 0

for p in points:
    if (p[0] - a)**2 + (p[1] - b)**2 <= R*R:
        count += 1

print(count)