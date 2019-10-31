import json

'''
x='{"name" : "William", "age":30,"city":"Indiana"}'
y=json.loads(x)
print (y['name'])

x={"name" : "William", "age":30,"city":"Indiana"}
y=json.dumps(x)
print (y)

print(json.dumps({"name":"Mike","age":12}))
print(json.dumps(["book",'pen']))
print(json.dumps(("book",'pen')))
print(json.dumps('hello'))
print(json.dumps(33))
print(json.dumps(14.3))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''
x={'name': 'orlando',
   'age':30,
   'married':True,
   'divorced':False,
   'children':('max','ele'),
   'pets':None,
   'cars':[
       {'model':'BMW 230','mpg':27.5},
       {'model':'Ford Edge','mpg':29.7}
   ]
   }
y=json.dumps(x)
print(y)
