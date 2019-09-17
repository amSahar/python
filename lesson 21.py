'''
set_1={'C++','Python','Java','Swift'}
print(len(set_1))
set_1.remove('C++')
set_1.discard('C++')
x=set_1.pop()
print(x)
set_1.pop()
set_1.clear()
del set_1
'''
set_1=set(('C++','Python','Java','Swift','html'))
set_2=set(('C++','Python','Java','Swift'))
set_3=set_1.difference(set_2)

print(set_3)

