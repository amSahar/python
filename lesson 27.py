x=600
y=400
z=500

'''
if y > x:
    print("y is greater than x")
elif x==y:
    print("x and y are equal")
else:
    print("x is greater than y")

print("TRUE") if x > y else print("FALSE")

if x<y and y==z:
    print ("both conditions are true") 

if x<y or y==z:
    print ("at least one conditions is true") 
'''

if x>y:
    print("x is greater than y")
    if x>z:
        print("elso greater than z")
    else:
        print("but not greater than z")
