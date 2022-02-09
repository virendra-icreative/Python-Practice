#recursion in Dictionary.
dictionary = {
    'elem01' : {
        1: 'A',
        2: 'B',
        3: 'C'
        },
    'elem02' : {
        1: 'D',
        2: 'E',
        3: {
            1: 'F',
            2: 'G',
            3: 'H'
        }
    }
}
dic_val = []
def rec_dict(dic):
    val = []
    for i,k in dic.items():
        if type(k) == dict:
            rec_dict(k)
        else:
            if i == 1:
                dic_val.append(k)

rec_dict(dictionary)
#dic_val.sort()
print(dic_val)