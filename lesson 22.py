dict_1={'sahar': 1996,
        'shahad': 1997,
        'lana': 2007}
'''
x=dict_1['sahar']
x=dict_1.get('sahar')
dict_1['lana']=2008
for x in dict_1:
    print(dict_1[x])

for x in dict_1.values():
    print (x)

print(dict_1.values())

for x,y in dict_1.items():
    print(x,y)
'''
print(dict_1.items())
