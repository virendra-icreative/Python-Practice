#recursion in List.
List = [12,45,13,14.5,12.6,'65','78',[75,4,62,'42','def',[84,96,'42.2',False]]]
def rec_list(obj):
    new_list = []
    for a in obj:
        try:
            new_list.append(float(a))
        except:
            try:
                new_list.extend(rec_list(a))
            except:
                pass
    return new_list

x = [int(x) for x in rec_list(List) if x%2==0]
print(x)

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
            2: {
                1:'G',
                2:'H',
                3:'I'
                },
            3: 'J'
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
                val.append(k)
    dic_val.extend(val)

rec_dict(dictionary)
dic_val.sort()
print(dic_val)