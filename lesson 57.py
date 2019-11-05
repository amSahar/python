import re

txt='I Love Python'
x=re.search('^I.*Python$',txt)

if (x):
    print('There is a match')
else:
    print('No match')
