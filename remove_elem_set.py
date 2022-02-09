#remove() in set
set1 = {'a','b','c','d','e'}
print(set1)
set1.remove('a')	#If the item to remove does not exist, remove() will raise an error.
print(set1)

#discard() in set
set1.discard('a')	#If the item to remove does not exist, discard() will not raise an error.
set1.discard('b')
print(set1)

#pop() in set
set1.pop()	#it reoves element rendomly couse set is unorganized
print(set1)

#clear() in set removes all the element of set
set1.clear()
print(set1)

#del in set deletes whole the set
del set1
#print(set1)