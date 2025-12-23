s = input()

a, op, b, _, c = s

def val(x):
    return None if x == 'x' else int(x)

a, b, c = val(a), val(b), val(c)

if a is None:     
    print(c - b if op == '+' else c + b)
elif b is None:     
    print(c - a if op == '+' else a - c)
else:             
    print(a + b if op == '+' else a - b)
