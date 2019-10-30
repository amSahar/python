'''
from mymodule import person

print (person["country"])


import mymodule as mx
a=mx.person['name']
print(a)


import mymodule as mx
mx.greeting('Eleven')
'''

import platform
import mymodule
print(platform.python_version())
print(platform.system())
print(dir(platform))
print(dir(mymodule))