import time
#using sep : separator
print('G', 'F', 'G', sep=' ')
var = 'Andy'
print('Name is', var)   #here ',' is saparator

#using end argument
print("python", end='@')
print("icreativetechnoles")

#using flush argument
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print('Start')