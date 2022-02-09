# def keyword use to define function.
def hello():
	print("Hello")
	
hello()

# yield Keyword used like return statement but is used to return a generator.
def fun():
    S = 0

    for i in range(1,6):
        S += i
        print(i,end=' : ')
        yield S

for i in fun():
    print(i)

# return keyword use ti return value from a function.
def add(a, b):
	return a + b

A = float(input("Enter num1 : "))
B = float(input("Enter num2 : "))
print(add(A, B))

# __doc__ prints the documentation of the function.
# which is defined in ..'''.. right after function defination
def fun(**x):
    '''Hello World!'''
    return x

print(type(fun()))

print(fun.__doc__)

# '*' prints tuple and '**' prints dictionary(pass pera meter as 'key=value' format)
def sum(*x,**y):
    return x,y

print(sum(10,15,20,a=15,b=25))