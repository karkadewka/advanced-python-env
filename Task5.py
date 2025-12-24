n = int(input())
letters = "ABCEHKMOPTXY"

for _ in range(n):
    s = input()
    ok = (
        len(s) == 6 and
        s[0] in letters and
        s[1:4].isdigit() and
        s[4] in letters and
        s[5] in letters
    )
    print("Yes" if ok else "No")
