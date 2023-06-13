from junie_twel import Sorting
import random


lst =[]
n= 20
for i in range(n):
    lst.append(random.randint(0, n*2))
    #lst.append(random.choice(['win', 'lose', 'draw']))
print(lst)
print(Sorting.default_sort(lst))

