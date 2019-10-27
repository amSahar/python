'''
def func(x):
    return lambda y:x*y
argu=func(2)

print (argu(5))
'''

def number (x):
    return lambda a : x * a

doubel_it=number(2)
triple_it=number(3)

print (doubel_it(100),triple_it(100))
