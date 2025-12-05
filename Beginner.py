# Assign multiple value
# Sequence unpackaging
a=[1,2,3]
x,y,z=a
print(x,y,z)
print(id(a))
print(id(x),id(y),id(z))
print(type(x),type(y),type(z))

"""
output:1 2 3
2169409659072
140723929707432 140723929707464 140723929707496
<class 'int'> <class 'int'> <class 'int'>
"""