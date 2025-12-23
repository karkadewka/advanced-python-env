items = input().split()

counts = {}
for x in items:
    counts[x] = counts.get(x, 0) + 1

print("Purchase:")
for k, v in counts.items():
    print(f"{k}: {v}")

most_popular = max(counts, key=counts.get)
print("\nMost popular:", most_popular)

print("\nPurchased:", *[k for k, v in counts.items() if v == 1])

print("\nSortedfrequency:")
for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
