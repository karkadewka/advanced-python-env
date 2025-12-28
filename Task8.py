n = int(input())
for i in range(1, n+1):
    ok = True
    for d in str(i):
        if d != '0' and i % int(d) != 0:
            ok = False
    if ok:
        print(i, end=" ")

a = list(map(int, input().split()))
print(a)
a[0], a[-1] = a[-1], a[0]
print(a)
