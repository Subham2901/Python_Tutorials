"""TUPLES ARE USED TO STORE MULTIPLE DATA UNDER ONE VARIABLE .
THEY ARE IMMUTABLE(UNCHANGEABLE) ADN THEY ARE REPRESENTED WITH SINGLE BRACKETS"""
x=(1,2,3,4,5,6,7,7,8)
print(x)
print(x[0])
"""As we know tuples are immutable thus we cannot alter the data inside a tuple once it is created"""
print(x.count(7))# to count the no of element in  a tuple
y=(4,5,6,723,7,8456,68,463,4)
print(x)
print(y)
z=x+y # we can concatenate two tuples into a third tuple by this method
print(z)
a=("python",)* 10 # by this technique we can store the same data multiple times inside a tuple
print(a)
print(max(x))# to print the max element inside the tuple
print(min(y)) # to print the minimum element inside the tuple
print(z)
del z # this will delelte the z tuple
#print(z)
"""Shown below is a process to edit or insert an element from the tuple.
we can similarly use the remove func to delete an element from a tuple but at first we need to convert the 
whole tuple into a mutable list"""
b=list(x)
print(b)
b.insert(2,"Python")
print(b)
x=tuple(b)
print(x)