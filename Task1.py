r = 5
circle = 3.14 * r * r
print(circle)
a = 4
b = 6
rectangle = a * b
print(rectangle)
arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6]

for arr in [arr1, arr2, arr3]:
    s = 0
    for x in arr:
        s += x
    print("sum =", s)
    print("avg =", s / len(arr))
