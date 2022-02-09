#try: , except, finally: , assert
a = 4
b = 0

# No exception Exception raised in try block
try:
	k = a//b 
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

# using assert to check for 0
print ("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print (a / b)