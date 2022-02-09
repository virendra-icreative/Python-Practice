#Sort it updates the list
List = [1,2,3,4,5,6,7,8,9,10]
def myFunc(x):
    return x%2 == 0
List.sort(reverse=True|False, key=myFunc)
print(List)

#Sorted it creates new list
List = [1,2,3,4,5,6,7,8,9,10]
x = sorted(List, key=myFunc, reverse=True)
print(List)
print(x)