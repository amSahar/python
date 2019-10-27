'''
def fun_ction (companies):
    for x in companies:
        print(x)

companies = ["iphone","samsung","huawei"]
fun_ction(companies)

def fun_ction(x):
    return 2*x
print (fun_ction(8))
print (fun_ction(7))
print (fun_ction(5))


def MyFunction (coffee, tea):
    print("I need "+coffee+" in breakfast")

MyFunction(coffee="black coffee",tea="trukish tea")

def MyFunction (*drinks):
    print("I need "+drinks[0]+" in breakfast")

MyFunction('black coffee','trukish tea')
'''
def try_rec(k):
    if (k>0):
        res=k+try_rec(k-1)
        print (res)
    else:
        res = 0
    return res

print ("Results:")
try_rec(5)




        
