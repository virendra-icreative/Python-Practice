#Dictionary Comprehension
k = ['a','b','c','d','e']
v = [25,15,14,1,16,45]
x = {k : v for (k,v) in zip(k,v)}
print(x)
dic = {x : x%2 for x in range(0,10,3)}
print(dic)