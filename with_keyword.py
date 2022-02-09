#with keyword is used to wrap the execution of block of code within methods defined by context manager.

with open('Python keywords/with_test', 'w') as file:
	file.write('Hello, Brother!{}'.format(chr(9970)))