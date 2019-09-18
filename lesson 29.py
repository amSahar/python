
majors=["Engineering","Science","IT"]

'''
for x in  "Engineering" :
    print(x)

for x in majors:
    print (x)

for x in majors:
    if x=="Science":
        break
    print (x)

for x in majors:
    print (x)
    if x=="Science":
        break
'''
for x in majors:
    if x=="Science":
       continue
    print (x)
