import random as rnd


for i in range(5):
    print(rnd.random())
    

print(rnd.randrange(5), end=' ')
print(rnd.randrange(5, 10), end=' ')
print(rnd.randrange(0, 10, 2), end=' ')
print(rnd.randint(0, 2))

n = [i for i in range(1, 11)]
print(rnd.choice(n))
print(rnd.sample(n, 5))
print(rnd.sample(n, 10))