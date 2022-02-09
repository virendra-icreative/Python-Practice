#break
for i in range (0,11,2):
	if i == 6:
		break
	else:
		print(i,end = ' ' )

print('\r')
#continue
a = 0
while a<=10:
	if a == 6:
		a += 2
		continue
	else:
		print(a,end = ' ' )
		a += 2