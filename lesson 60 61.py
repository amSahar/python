import json
import re

my_tuple=('sat','sun','mon','tue','wed','thur','fri')
x=json.dumps(my_tuple)
print(x)

txt=('Data is the new oil')
x=re.search('Data',txt)
if (x):
    print('There is a match!',x.span())
else:
    print('No match')