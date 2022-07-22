data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
data_tuple = tuple(data)
for i in data_tuple:
    if  i.isalpha():
        designations.append(i)
    else:
        codes.append(i)
operators = {}
c = 0
while len(operators) != len(designations):
    operators[designations[c]] = codes[c]
    c+=1
del operators ['Katel'], operators['Fonex']
operators ['O!'] = {'0700', '0502', '0508'}
operators ['Beeline'] = {'0770', '0222', '0777'}
operators ['Megacom'] = {'0550', '0557', '0554'}
for k, v in operators.items():
    print(f'{k} - {v}')



