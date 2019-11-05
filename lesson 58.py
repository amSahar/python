import re


txt=('If there is more than one match, only the first occurrence of the match will be returned')

x=re.findall('the',txt)

print(x)

if(x):
    print("There is at least on match")
else:
    print("No match")

str=' you can do it '
x=re.search('\s',str)

if (x):
    print ('the first white space locat in pos:', x.start())
else:
    print('No white space')

str=' you can do it '
x=re.split('\s',str)
print(x)