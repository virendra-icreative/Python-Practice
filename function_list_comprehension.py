l = [15,12,14,13,'15','12','asd',12.14]
new_l = []
def convert_int(a):
    for x in a:
        try:
            new_l.append(float(x))
        except:
            pass
    return new_l

x = [x for x in convert_int(l) if x%2==0]
print(x)