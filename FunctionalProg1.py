#Lambda functions
p = lambda n : n**3
print(p(4))

lst1 = [10, 20, 30, 40, 50]
print((lambda l : sum(l)/len(l))(lst1))

#Map function
lst = [1, 2, 3, 4, 5]
result = list(map(lambda x : x*x, lst))
print(result)

#Reduce function
from functools import reduce
def sum(a,b) :
    return a+b
def prod(a,b) :
    return a*b
lst1 = [1, 2, 3, 4, 5]
s = reduce(sum, lst1)
p = reduce(prod, lst1)
print(lst1, s, p)

#filter function
lst2 = [10, 15, 20, 25, 30]
result2 = list(filter(lambda x : x%10==0, lst2))
print(result2)

#Using all three higher order functions
def sqr_g1000(n) :
    return n > 1000
lst = [10, 20, 30, 40, 50]
y = list(filter(sqr_g1000, map(lambda x : x*x, lst)))
print(y)
