from random import randint
lst = [randint(-100, 100) for i in range(10)]
print(lst)
lst[2] = [randint(-100, 100) for i in range(1)]
del lst[6]
print(lst)
