counts = {' ': 0}
name = "Leonardo"

for c in name:
    if c not in counts:
        counts[c] = 0
    counts[c] += 1

print(counts)

aliens = {}
