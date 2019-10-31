import json

x = {'name': 'orlando',
     'age': 30,
     'married': True,
     'divorced': False,
     'children': ('max', 'ele'),
     'pets': None,
     'cars': [
         {'model': 'BMW 230', 'mpg': 27.5},
         {'model': 'Ford Edge', 'mpg': 29.7}
     ]
     }

print(json.dumps(x, indent=4 , separators=(". "," = ")))
#print(json.dumps(x, indent=4 , sort_keys=True))
