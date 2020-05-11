"""A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
Its an unordered collection with no duplicate elements and no indexing
"""
a={1,4,2,6,5,8}
print(a)
b={2,3,4,4,5,6}
print(b)
c={1,1,4,5,62,3,}
print(c)
d={9,8,7,6,5,2,2,2,2}
print(d)
"""Thus we can notice that no matter how we will insert the data it will automatically 
delete the duplicate elements and sort into ascending order"""
"""some inbuilt func of the set"""
a.clear()# clear the data preent in the set
print(a)
a.add(1)# add elements in the set
print(a)
a.update([2,3, 4,5,6,7,9,8])# by this we can add multiple elements into the set
print(a)
a.remove(4) # remove an element from the set
print(a)
a.discard(3)# remove an element from the set
a.pop() # in this case it will remove any random element from the set
print(a)
a=set((2,3,4,5,6,7))# using set constructor also we can create a set
print(a)
"""Just like mathematics we can use the same operations in our set also ,they are as follow"""
b={7,8,9,10,11,20}
print(a|b)# this gives the union of the elements of the two sets
print(a.union(b))# by this method also we can find the union of the two set
print(a&b)# to find the intersection of the two sets
print(a.intersection(b))# by this method also we can find the intersection
print(a-b)# to find the elements that are only in a but not in a
print(a.difference(b))# this will also find the elements that are only on a but not on b
print(b-a)# to find the elements that are only present in b
print(b.difference(a))# this will also print the elements that are only present in b
print(a^b)# this will show the symetric difference
print(b^a)
print(a.symmetric_difference(b))# this will show the symetric diff
""" it do not have any indexing therefore we cannot access the elements using the indexes of the set
THERE ARE MORE METHODS PLEASE REFER TO THE DOCUMENTATION FOR FURTHER UPDATES"""

