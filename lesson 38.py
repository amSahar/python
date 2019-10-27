'''
subjects=['math','english','art']

for x in subjects:
    print(x)

subjects=['math','english','art']
subjects.append('sicence')
print(subjects)

subjects=['math','english','art','sicence']
subjects.pop(3)
print(subjects)


subjects=['math','english','art','sicence']
subjects.remove('sicence')
print(subjects)
'''
subjects=['math','english','art','sicence']
x=subjects.copy()
print(x)
