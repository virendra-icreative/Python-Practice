import sys

#sys.stdout used to display output directly to the screen console
sys.stdout.write('Aslan\n')
#sys.stdin used to get input from the command line directly.
for line in sys.stdin:
    if line.rstrip() == 'q' or line.rstrip() == 'Exit':
        break
    print(f'Input : {line}')
print('Exit')

#Whenever an exception occurs in Python it is written to sys.stderr
def print_to_stderr(*a):
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file = sys.stderr)
 
print_to_stderr("Hello World")