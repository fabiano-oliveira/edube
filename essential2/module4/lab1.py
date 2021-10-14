import os

content = 'cBAbAa'
set = {}

for c in content:
    c = c.lower()
    if c.isalpha():
        set[c] = set.get(c, 0) + 1

print(sorted(set.items(), key=lambda item: -item[1]))

print(os.name)

