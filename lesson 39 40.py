
def rec(x):
    if x == 0:
        return 1
    else:
        return 5 * rec(x-1)

    
print("Result = " ,rec(3))


num =[ 88 ,9 ,7 ,3 ,2 ,-1 ,-5 ,-6 ,-4]

b = lambda a: a > 0

for x in num:
    if(b(x)) : print(x)
