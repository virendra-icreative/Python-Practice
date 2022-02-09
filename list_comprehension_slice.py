#List comprehension
x = [x for x in range(1,20,2)]
print(x)
x = [x for x in range(1,20,2) if x % 3 == 0]
print(x)

a = 'aslan'
a = [a for a in a]
print(a)

b = 'lycan'
b = [b.capitalize() for b in b]
print(b)

lst = list(range(1,10))
print(lst)
#slicing in list
lst1 = lst[2:8]
print(lst1)

lst2 = lst[2:8:2]
print(lst2)