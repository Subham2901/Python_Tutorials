""" LIST- IT IS  A KIND OF COLLECTION WHICH ALLOWS US TO STORE
 MANY VALUES UNDER ONE VARIABLE.A list is a collection which is ordered
 and changeable. In Python lists are written with square brackets."""
x=[3,6,8,4,7,10] # the list defination,here each nos are known as elements of the list.
print(x)
print(x[0:3])# each element of the list are assigned with  a particular index
y=['python',4,5,23,[1,2,3,4,4,5],6,7,8]
print(y[0]) # we can store a string inside a list by using inverted commas
print(y[4])# we can store a list inside a list by using third brackets
print(y[-1])# We can directly access the last element of the list by using (-1).
print(len(x))# by using inbuilt func (len) we can find the length of the element
x.insert(2,'action')# takes the index no, where we want to insert the element along with the element that we want to insert
print(x)
x.remove('action')#it just removes the mentioned element from the list
print(x)
x.pop()# to pop the last element of out of the list
print(x)
x.append(10)# to insert an element at the end of the list.
print(x)
s=x.copy()# to copy the elements of the list
print(s)
x.clear()# to delete all the elements of the list
print(x)
del x # to delete the whole
#print(x)
y=[1,10,45,6,2,6,8,3,7,66,88]
y.sort() # to sort the element of the list into ascending order
print(y)
y.reverse()#to reverse the order of the list
print(y)
print(y.count(6))# to create the no of elements present in the list.

"""Except for these there are more inbuilt functions present for the list .
please refer to the python documentary for further details."""