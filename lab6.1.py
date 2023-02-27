import random

a = tuple(random.randint(0, 5) for i in range(10))
b = tuple(random.randint(-5, 0) for i in range(10))
c = a + b

print(c)
print(c.count(0))