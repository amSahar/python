
'''
dict_1={'student1': {'sahar': 1996},
        'student2': {'shahad': 1997},
        'student3': {'lana': 2007}
        }

dict_2=dict_1.copy()
dict_1.popitem()

dict_2=dict(dict_1)

print(dict_1)

student1= {'sahar': 1996}
student2= {'shahad': 1997}
student3= {'lana': 2007}

students={ 'student1' : student1,
           'student2' : student2,
           'student3' : student3,
         }
print(students)
'''

dict_1 = dict(sahar=1996,department='CE')

x=dict_1.get('sahar')
print(x)












