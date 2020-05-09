"""Definiton: A variable is a storage location(identified) by a memory location/addrress)
paired with an associated symboloic name(an identifier),which contains some known or unkmnown quantity of information
 refered to as value
i.e It's an named memory location which can be used to store information which can be later retrieved by using that name
As python is a dynamically typed language we don't need to declare the type of the vairalble
before using it.But we must assign a value to detect the type of the variable"""
""" Rules of naming a variable:-
1.It must start with a letter or an underscore
2.It can only consists of letters & numbers & underscores.
3.It is case Sensitive
<variable name> <assigment operatora(=)> <value>
"""

b = 10
print(b)

"""except for that we cannot use the reserve words for declaring variables 
    THE RESERVED WORDS ARE:
   and """

myInt=10 # stores integer type data
print(myInt)

myFloat=10.5 #stores float type data
print(myFloat)

mycomplex=1j #stores complex type data
print(mycomplex)

myNum=10e2 #e symbolises exponent symbol
print(myNum)

myNum=10E2 # caps E also symbolises exponent symbol
print(myNum)

mytstr="Subham Singh "# we can store strings into a varialble using double quotes

myStr='loves python' # we can store strings using single quotes too

Mystr=mytstr+myStr # we can add or concatenate two strings just by adding a + sign between them

print(Mystr)

"""Now let us see an another problem"""
myFloat=myInt
print(myFloat)
myInt=myFloat
print(myInt)


"""We will notice in both the cases the output is 10,that means when converting from 
integer to float the type has not changed but when we converted from float to int it got converted automatically or implictly
 THUS TO OVERCOME THIS ISSUE WE WILL USE EXPLICIT TYPECASTING """

myFloat=float(myInt)# by using explicit typecasting we have changed the type succesfully
print(myFloat)

"""type is an inbuilt functon of python use to display the data type off the variables"""

print(type(myFloat))#this will print the type of the data which is stored in the variable myFloat

