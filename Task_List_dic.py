a = [1,2,3]

b = {
	1: [4,5,6],
	2: [7,8],
	3: [9, 10],
	4: [11, 12, 13],
	9: [14, 15],
	10: [16],
	13: [19, 20],
	19: [21]
}

List = []
def fun(L):
    for i in L:
        List.append(i)
        for k,v in b.items():
            if k==i:
                fun(v)
fun(a)
print(List)