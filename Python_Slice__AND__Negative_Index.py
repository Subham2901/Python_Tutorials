"""Slice Function-slice() is a constructor
that creates a Python Slice object to
represent the set of indices that
range(start, stop, step) specifies.
With this, we can slice a sequence like a
string, a tuple, a list, a range object, or
a bytes object."""
a=[1,2,3,4,5,6,7,8,9,10]
b={0,1,2,3,4,5,6,7,8,9,10}
c="01234567891011"
"""x=slice(start,end,step)This is the format of a slice funtion """
x=slice(0,5)
print(a[x])
x=slice(0,7,2)
print(a[x])
"""There's another short notation for using slice function, By using Third brackets[starting index:end index:step]
 along with colon we implement slice function. """
print(a[0:5])# this will print the elements present in the list from zeroth index till (5-1)index
print(a[:])# this will print all the elements in the list
print(a[0:6:2])# this will print all the elements from 0th index till (6-1)th index with step (2)
"""NEGATIVE INDEXING- This is a kind of indexing where (-1) denotes the last element of the list or the 
tuple or the string"""
print("---------------------------------------------------------------------")
print(a[-1])# this will print the last element of the list
print(a[::-1])# this will print all the element of the list in the reverse order.
print(a[1::-1])# This will print all the element of the list starting form index one in reverse order
print(a[:])
print(a[:-4:-1])#This will print all the element from the last till index no mentioned)

