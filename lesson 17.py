'''
tuple_1=('python',) *10

if "3.14" in tuple_1:
    print ("True")

tuple_1=('python', 'بايثون', 'java', '3.14')
tuple_2=('python', 'بايثون', 'java', '3.14','hi')
tuple_3=tuple_1+tuple_2
print (tuple_3)

x=(2,3,1,4)
x+=(1,4,7)

tuple_1=('python', 'بايثون', 'java', '3.14')
print(len(tuple_1))

tuple_1=tuple(('python', 'بايثون', 'java', '3.14'))
print(tuple_1)
'''
tuple_1=('python', 'بايثون', 'java', '3.14')
a=tuple_1.count('java')
b=tuple_1.index('3.14')
print(a)
print(b)
