import math

a = int(input(":"))
b = int(input(":"))
c = (a*a + b*b) ** 0.5

x = int(input(":"))
y = int(input(":"))
d = (x*x + y*y) ** 0.5

print(c)
print(d)

if c > d:
    print("1st is bigger")
else:
    print("2nd is bigger")

s = input("Write ur string:")
words = s.split()
for w in words:
    print("".join(sorted(w)), end=" ")
