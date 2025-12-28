import math

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

a1, b1 = map(float, input("Triangle 1:").split())
a2, b2 = map(float, input("Triangle 2:").split())

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypo1:", h1)
print("Hypo2:", h2)

if h1 > h2:
    print("1st is greater")
else:
    print("2nd is greater")

s = input("Enter string: ")
words = s.split()
sorted_words = ["".join(sorted(w)) for w in words]
print(" ".join(sorted_words))