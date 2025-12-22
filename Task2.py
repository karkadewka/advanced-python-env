a = input()
b = input()

bb = b + b
n = len(b)

print(sum(a[i:i+n] in bb for i in range(len(a) - n + 1)))
