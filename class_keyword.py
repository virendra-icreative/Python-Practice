class test:
	item = 'apple'
	price= 250

	def sum(self):
		print('tThis function is for sum of to integer.')
		a = int(input("Enter num1 : "))
		b = int(input("Enter num2 : "))
		print(a + b)

class1 = test()

print(class1.item)
print(class1.price)
class1.sum()  #here is an error.