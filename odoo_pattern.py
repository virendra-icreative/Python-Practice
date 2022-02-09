class ANSI():
	def color_text(code):
		return "\33[{code}m".format(code=code)

for i in range(7):
#O
    for j in range(7):
        if (i in[2,3,4] and j in [2,3,4]) or (i in [0,6] and j in [0,6]):
            print(' ',end=' ')
        else:
            print(ANSI.color_text(33) + '*',end=' ')
    
    for j in range(2):
        print(' ',end=' ')
#D
    for k in range(7):
        if (k in [2,3] and i in range(2,5)) or (k == 6 and i in [0,6]):
            print(' ',end=' ')
        else:
            print(ANSI.color_text(31) + '*',end=' ')
            
    for j in range(2):
        print(' ',end=' ')
#O
    for j in range(7):
        if (i in[2,3,4] and j in [2,3,4]) or (i in [0,6] and j in [0,6]):
            print(' ',end=' ')
        else:
            print(ANSI.color_text(33) + '*',end=' ')

    for j in range(2):
        print(' ',end=' ')
#O  
    for j in range(7):
        if (i in[2,3,4] and j in [2,3,4]) or (i in [0,6] and j in [0,6]):
            print(' ',end=' ')
        else:
            print(ANSI.color_text(33) + '*',end=' ')

    print('')