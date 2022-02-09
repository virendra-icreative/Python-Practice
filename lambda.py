'''Lambda() keyword is used to make inline returning 
functions with no statements allowed internally.'''
a = lambda x: x*x*x
b = lambda x: x*x
c = lambda x: x%2

e = float(input("Enter Number : "))
print("It's a cube of number : ",a(e))
print('It\'s a multiplication of number : ',b(e))

print("Enterned nuber is even") if c(e) == 0  else print('Enterned number is odd')