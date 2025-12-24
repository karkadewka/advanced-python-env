s = input()

print(sum(s[i:i+5] in (">>-->", "<--<<") for i in range(len(s))))


