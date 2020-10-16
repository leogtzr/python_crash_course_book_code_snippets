from collections import Counter


def print_keys(counts):
    for k, _ in counts.items():
        print(counts[k])


counts = Counter()
name = "Leonardo"

for c in name:
    counts[c] += 1

print(counts['o'])

del counts['o']

print(counts['o'])
print(counts)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~>")

# Iterating keys and values:
for k, v in counts.items():
    print(k)


# Iterating 2:

print("###############")

for kv in counts:
    print(kv)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print_keys(
    {
        'x': 23,
    }
)
