'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield']
'''
import keyword
  
#printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

print('''\nTrue: This keyword is used to represent a boolean true. If a statement is true, “True” is printed.
False: This keyword is used to represent a boolean false. If a statement is false, “False” is printed. 
None: This is a special constant used to denote a null value or a void. It's important to remember, 0, any empty container(e.g empty list) does not compute to None. 
It is an object of its datatype - NoneType. It is not possible to create multiple None objects and can assign them to variables.''')

print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])