A = int(input())
B = int(input())
C = int(input())
D = int(input())

num = A*D - C*B
den = B*D

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(abs(num), den)
print(num//g, "/", den//g)


n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
