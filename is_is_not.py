x = 1001
y = 1001
if x is y:
    print('True')
    print(id(x), " and ", id(y))
else:
    print('False')
    print(id(x), " and ", id(y))