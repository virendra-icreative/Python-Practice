dictionary = {
	'product' : 'car',
	'model' : 7596,
	'sels' : 542
}

x = dictionary['product']
print(x)

#get() method

x = dictionary.get('model')
print(x)

#keys() method will return a list of all the keys in the dictionary.
x = dictionary.keys()
print(x)

#values() method will return a list of all the values in the dictionary.
x = dictionary.values()
print(x)

#items() method will return each item in a dictionary, as tuples in a list.
x = dictionary.items()
print(x)

#change values or add new key:value in dictionary.
dictionary['model'] = 8050
print(x)

dictionary['lose'] = 45000
print(x)