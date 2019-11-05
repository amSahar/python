import re
txt='YOU CAN DO IT !'
x=re.sub('\s','_',txt)
print(x)

txt='YOU CAN DO IT !'
x=re.sub('\s','_',txt,2)
print(x)

txt='I Love Python'
x=re.search('o',txt)
print(x)

txt='I Love Python'
x=re.search(r'\bP\w+',txt)
print(x.span())

txt='I Love Python'
x=re.search(r'\bP\w+',txt)
print(x.string)

txt='I Love Python'
x=re.search(r'\bP\w+',txt)
print(x.group())


