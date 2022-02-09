#there is two ways to define nested dictionary.
nest_dic = {
	'item1' : {
	'name' : 'apple',
	'sels' : '500kg'
	},
	'item2' : {
	'name' : 'graps',
	'sels' : '800kg'
	},
	'item3' : {
	'name' : 'mango',
	'sels' : '1500kg'
	}
}

print(nest_dic)
for i in nest_dic:
	print(nest_dic[i])

item1 = {
	'name' : 'apple',
	'sels' : '500kg'
},
item2 = {
	'name' : 'graps',
	'sels' : '800kg'
},
item3 = {
	'name' : 'mango',
	'sels' : '1500kg'
}

test_dic  = {
	'item1' : item1,
	'item2' : item2,
	'item3' : item3
}

print(test_dic)