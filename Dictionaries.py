"""Dictionaries can be defined as a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
dictionary={'key':"value'}
we can access each values by their keys"""
dict={'name':'Subham','year':1999,'age':21}
print(dict)
print(dict['name'])# by using the key we can access the value
"""In a dictionary,as key or as value , we can define any data types"""
b={'name':'Subham',1999:1999,20.20:4,True:False}
print(b['name'])
print(b[True])
print(len(b))
print(b.get('name'))
b['surname']='Singh'
print(b)
b.pop('surname')
print(b)
dict.clear()
print(dict)
del dict
b['name']='Reek'
print(b)
b.update({'name':'Subham'})
print(b)
print(b.values())
print(b.keys())
print(b.items())
b.popitem()
print(b)


