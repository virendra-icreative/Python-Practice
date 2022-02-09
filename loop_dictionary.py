test_dic = {
	'product' : 'car',
	'model' : 7596,
	'sels' : 542
}

a = test_dic.items()
#print(a)

#looping through 'for'
for i in test_dic:
	print(i)
print('\n')

#print keys through 'for'
for i in test_dic.keys():
	print(i)
print('\n')

#print values through 'for'
for i in test_dic.values():
	print(i)
print('\n')

#print all items using 'for'
for i, j in test_dic.items():
	print(i ,'\t', j)