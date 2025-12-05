# create new object for immutable 
x=y=z="orange"
print(id(x),id(y),id(z))
y="green"
print(id(x),id(y),id(z))

print(x,y,z)
"""
output:
2273638276560 2273638276560 2273638276560
2273638276560 2273643917696 2273638276560
orange green orange"""