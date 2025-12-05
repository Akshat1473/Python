# create new object for mmutable 
x=y=z=[1,2,3]
print(id(x),id(y),id(z))
y[0]=8
print(id(x),id(y),id(z))

print(x,y,z)
"""
output:
1760921477312 1760921477312 1760921477312
1760921477312 1760921477312 1760921477312
[8, 2, 3] [8, 2, 3] [8, 2, 3]"""