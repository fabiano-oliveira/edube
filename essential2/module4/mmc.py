
d = 35
count = 0

for i in range(1000, 10000):
    if i % d == 0 and i % 10 == 0:
        count += 1

print(count)
