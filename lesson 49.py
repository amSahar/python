'''
x=500
def func():
    x=100
    print(x)
func()
print(x)


def func():
    global x
    x=100

func()
print(x)
'''

x=200

def func():
    global x
    x=900
func()
print(x)
