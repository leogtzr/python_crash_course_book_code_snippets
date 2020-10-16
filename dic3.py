from collections import Counter
from sys import exit
#import sys

count = Counter()

for c in "Leonardo":
    count[c] += 1

print(count)

exit(1)
