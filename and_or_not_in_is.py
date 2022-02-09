#logial operator and, or, not.
print(True and False)
print(True or False)
print(not True)

#'in' to check in text or container
if 'apple' in 'eat apples every day.':
	print('apple is in text.')

#'in' for looping.
for i in range(5):
	print(i,end = " ")

#using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print('\n')
print(' ' is ' ')
print('asd' is ' ')

#using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})