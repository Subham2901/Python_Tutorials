 #python Strings
x="hello world" # method 1
print(x)
y='hello world' #method 2
print(y)
"""/ is known as escape character we can use this in the following 
way shown"""
z='hello\'s world'
print(z)
a="hello\"s world"
print(a)
b=" h e ll o world"
c="1234"
d='2.5'
"""-------------------------------------------------------------------------------------"
Some inbuilt Methods of the string"""
print(x.upper()) # to convert eveything to uppercase
print(x.lower()) # to convert everything to lowercase
print(x[0]) # to print only the characters we want
print(x[0:3]) # to print the characters specified by the index
print(x.strip()) # to remove the extra spaces at the starting and at the ending of the string
print(x.islower()) # Returns a boolean value used to check wheather all the characters in the string are in lower case or not
print(x.isupper()) # Used to check whether all the characters of the string are in upper case or not.
print(x.replace('h','m'))# used to replace the character with the characters of our choice from the string
print(b.split(' '))# used to split the characters of the string into an arrau.
print(x * 100) # by this process we can print a string multiple times
print(c.isnumeric()) # to check whether all the characters of the string are numeric or not. Returns true if yes.
print(d.isdecimal())# to check  whether all the characters of the string are decimal values or not.
print(b.count('o'))# used to count the  no of occurances of the substring goven by the user.
"""There are more inbuilt functions for that we can check the python documentary"""
