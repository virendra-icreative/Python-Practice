#Modulo operator
print("ID : %2d, Price : %10.2f" % (1312,7500))
print('%5o' % (47))
print("%10.3E" % (356.05514))

#format() mathod
print('I am {}, and {} years old.'.format('Andy', 25))
print('I am {1}, and {0} years old.'.format('Andy', 25))
print('I am {name}'.format(name = 'Ana'))
num1 = 15.1568
print('Num1 = {0:5.2f}, Num2 = {num2:.2f}'.format(num1, num2 = 12.13))
#dictionary in forma()
dic = {'name' : 'Aslan', 'age' : 26}
print('I am {0[name]}, and {0[age]} years old.'.format(dic))
print('I am {age}, and {name} years old.'.format(**dic))

#f-String
name, age = 'Andy', 47
print(f'I am {name}, and {age} years old.')