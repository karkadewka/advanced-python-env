a, _ = map(int, input().split())
h = a * 1.73 / 2
triangle = a * h / 2
hexagon = triangle * 6
print(hexagon)

for i in range(3):
    x, y = map(int, input().split())
    print(x * y)
