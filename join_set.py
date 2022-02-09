#union in set returns a new set with all items from both sets:
set1 = {'a','b',2,4,'c','d'}
set2 = {'a','c',1,2,3,4}
set3 = set1.union(set2)
print(set3)

#update() method inserts the items in set2 into set1:
set1.update(set2)
print(set1)

#intersection() method will keep only the items that are present in both sets.
x = {'a', 'b', 'c'}
y = {'d','e','a'}

z = x.intersection(y)
print(z)

#intersection_update() method will keep only the items that are present in both sets.
x.intersection_update(y)
print(x)

#symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
a = {'a', 'b', 'c'}
b = {'d','e','a'}

c = a.symmetric_difference(b)
print(c)

#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
a.symmetric_difference_update(b)
print(a)